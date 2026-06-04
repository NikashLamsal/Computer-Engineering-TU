import math
import random
import tkinter as tk
from tkinter import messagebox


class DynamicCSP10NodesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic CSP Playground (10 Nodes Layout)")
        self.root.geometry("900x650")
        self.root.configure(bg='#1e1e24')

        # Colors available for selection (Palette)
        self.colors = ['#FF5252', '#4CAF50', '#2196F3', '#FFEB3B']  # Red, Green, Blue, Yellow
        self.color_names = ['Red', 'Green', 'Blue', 'Yellow']
        self.selected_color = self.colors[0]

        # CSP Variables
        self.num_nodes = 10
        self.nodes = [f"N{i}" for i in range(1, self.num_nodes + 1)]
        self.coords = {}        # {'N1': (x, y)}
        self.topology = {}      # {'N1': ['N2', 'N3']}
        self.assignments = {}   # Active solutions: {'N1': '#FF5252'}

        self.create_widgets()
        self.generate_10_node_graph()

    def create_widgets(self):
        # --- Top Control Panel ---
        control_frame = tk.Frame(self.root, bg='#2a2a35', pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)
        
        gen_btn = tk.Button(
            control_frame, text="🎲 Generate New 10-Node Map", font=('Arial', 11, 'bold'),
            bg='#9C27B0', fg='white', command=self.generate_10_node_graph, relief=tk.FLAT
        )
        gen_btn.pack(side=tk.LEFT, padx=15)

        solve_btn = tk.Button(
            control_frame, text="🤖 AI Auto-Solve", font=('Arial', 11, 'bold'),
            bg='#4CAF50', fg='white', command=self.run_ai_solver, relief=tk.FLAT
        )
        solve_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = tk.Button(
            control_frame, text="🧹 Clear Colors", font=('Arial', 11),
            bg='#555566', fg='white', command=self.clear_assignments, relief=tk.FLAT
        )
        clear_btn.pack(side=tk.LEFT, padx=5)

        # --- Side Color Selection Palette ---
        palette_frame = tk.Frame(self.root, bg='#2a2a35', width=150, padx=15, pady=20)
        palette_frame.pack(side=tk.LEFT, fill=tk.Y)

        palette_label = tk.Label(
            palette_frame, text="SELECT COLOR", font=('Arial', 10, 'bold'), 
            bg='#2a2a35', fg='#B0BEC5'
        )
        palette_label.pack(anchor=tk.W, pady=(0, 15))

        self.color_var = tk.StringVar(value=self.colors[0])
        for i, color in enumerate(self.colors):
            frame = tk.Frame(palette_frame, bg='#2a2a35', pady=6)
            frame.pack(fill=tk.X)
            
            rb = tk.Radiobutton(
                frame, text=self.color_names[i], variable=self.color_var, 
                value=color, bg='#2a2a35', fg='white', selectcolor='#2a2a35',
                font=('Arial', 11), command=self.update_selected_color
            )
            rb.pack(side=tk.LEFT)
            
            canvas_indicator = tk.Canvas(frame, width=20, height=20, bg=color, highlightthickness=0)
            canvas_indicator.pack(side=tk.RIGHT, padx=5)

        # --- Graphics View Canvas ---
        self.canvas = tk.Canvas(self.root, bg='#121214', highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.handle_canvas_click)

    def generate_10_node_graph(self):
        """Generates a stable, non-overlapping 10-node layout using Grid Anchors."""
        self.assignments.clear()
        self.coords.clear()
        self.topology.clear()

        # Define 12 possible logical sectors on canvas (4 columns x 3 rows grid map)
        cols, rows = 4, 3
        cell_width = 700 // cols
        cell_height = 550 // rows
        
        sectors = [(c, r) for c in range(cols) for r in range(rows)]
        # Pick 10 random sectors out of the 12 to place our 10 nodes
        chosen_sectors = random.sample(sectors, self.num_nodes)

        # Generate coordinates with local jitter inside their sector bounds
        for idx, node in enumerate(self.nodes):
            sc_col, sc_row = chosen_sectors[idx]
            
            # Compute sector center coordinates
            base_x = int((sc_col + 0.5) * cell_width) + 30
            base_y = int((sc_row + 0.5) * cell_height) + 30
            
            # Inject a small random offset (jitter) to keep the layout feeling dynamic
            x = base_x + random.randint(-20, 20)
            y = base_y + random.randint(-20, 20)
            
            self.coords[node] = (x, y)
            self.topology[node] = []

        # Generate a realistic tree/mesh topology network
        for i, node in enumerate(self.nodes):
            # Sort all other nodes by physical distance from current node
            distances = [(target, math.hypot(self.coords[node][0] - self.coords[target][0], 
                                            self.coords[node][1] - self.coords[target][1]))
                         for target in self.nodes if target != node]
            distances.sort(key=lambda item: item[1])

            # Force connect to closest neighbor to guarantee no node is isolated
            closest_neighbor = distances[0][0]
            if closest_neighbor not in self.topology[node]:
                self.topology[node].append(closest_neighbor)
                self.topology[closest_neighbor].append(node)

            # Randomly attach to secondary neighbors to build complex constraints
            num_extra_edges = random.randint(1, 2)
            for j in range(1, min(num_extra_edges + 1, len(distances))):
                candidate = distances[j][0]
                # Enforce max degree limits (max 3 edges per node) to maintain planar colorability
                if len(self.topology[node]) < 3 and len(self.topology[candidate]) < 3:
                    if candidate not in self.topology[node]:
                        self.topology[node].append(candidate)
                        self.topology[candidate].append(node)

        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")
        
        # Draw constraints edges
        drawn_edges = set()
        for node, neighbors in self.topology.items():
            for neighbor in neighbors:
                edge = tuple(sorted((node, neighbor)))
                if edge not in drawn_edges:
                    x1, y1 = self.coords[node]
                    x2, y2 = self.coords[neighbor]
                    self.canvas.create_line(x1, y1, x2, y2, width=3, fill='#37474F')
                    drawn_edges.add(edge)

        # Draw structural node bodies
        for node, (x, y) in self.coords.items():
            color = self.assignments.get(node, '#3A3A4A')  # Dark gray if unassigned
            
            # Nodes rendering radius set to 22 pixels
            self.canvas.create_oval(x-22, y-22, x+22, y+22, fill=color, outline='#78909C', width=2)
            self.canvas.create_text(x, y, text=node, font=('Arial', 10, 'bold'), fill='white')

    def update_selected_color(self):
        self.selected_color = self.color_var.get()

    def handle_canvas_click(self, event):
        """Processes human node interaction and triggers adjacency logic confirmation checks."""
        clicked_node = None
        for node, (x, y) in self.coords.items():
            if math.hypot(event.x - x, event.y - y) <= 22:
                clicked_node = node
                break

        if clicked_node:
            if self.is_consistent(clicked_node, self.selected_color):
                self.assignments[clicked_node] = self.selected_color
                self.draw_graph()
            else:
                messagebox.showwarning(
                    "Constraint Violation", 
                    f"Conflict detected! An adjacent linked node is already colored {self.get_color_name(self.selected_color)}."
                )

    def get_color_name(self, hex_code):
        return self.color_names[self.colors.index(hex_code)]

    # --- Backtracking CSP Engine Loop Core ---
    def is_consistent(self, variable, value):
        for neighbor in self.topology.get(variable, []):
            if neighbor in self.assignments and self.assignments[neighbor] == value:
                return False
        return True

    def select_mrv_variable(self):
        unassigned = [v for v in self.nodes if v not in self.assignments]
        if not unassigned: return None
        
        def count_legal_values(var):
            return sum(1 for val in self.colors if self.is_consistent(var, val))
            
        return min(unassigned, key=count_legal_values)

    def backtrack(self):
        if len(self.assignments) == len(self.nodes):
            return True

        var = self.select_mrv_variable()
        if var is None: return False

        for value in self.colors:
            if self.is_consistent(var, value):
                self.assignments[var] = value
                
                # Dynamic refresh pipeline interface
                self.root.update()
                self.root.after(80)  # slightly faster calculation playback for 10 nodes scale
                self.draw_graph()

                if self.backtrack():
                    return True
                    
                del self.assignments[var]
                self.draw_graph()
                
        return False

    def run_ai_solver(self):
        self.assignments.clear()
        if self.backtrack():
            messagebox.showinfo("Solver Complete", "Success! The AI Backtracking algorithm resolved all 10 nodes cleanly.")
        else:
            messagebox.showerror("Solver Error", "Failed to compute a valid mapping solution.")

    def clear_assignments(self):
        self.assignments.clear()
        self.draw_graph()


if __name__ == "__main__":
    main_window = tk.Tk()
    app = DynamicCSP10NodesGUI(main_window)
    main_window.mainloop()