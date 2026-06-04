import time
import tkinter as tk
from tkinter import messagebox


class TreeNode:
    def __init__(self, name, x, y):
        self.name = name          # Unique Identifier (e.g., 'A', 'B', 'C')
        self.x = x                # Canvas X coordinate
        self.y = y                # Canvas Y coordinate
        self.children = []        # Sub-nodes linked below


class TreeBacktrackDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Tree Search & Backtracking Dashboard")
        self.root.geometry("950x650")
        self.root.configure(bg='#1A1A24')

        # Control States
        self.search_target = ""
        self.path_taken = []      # Active tracking stack framework
        self.visited_nodes = set()

        self.create_tree_structure()
        self.create_widgets()

    def create_tree_structure(self):
        """Constructs a deterministic tree with 15 nodes and a depth of 5."""
        # Layer 1: Root (Depth 1)
        self.root_node = TreeNode("Root", 475, 50)

        # Layer 2: (Depth 2)
        b1 = TreeNode("B1", 250, 150)
        b2 = TreeNode("B2", 700, 150)
        self.root_node.children = [b1, b2]

        # Layer 3: (Depth 3)
        c1 = TreeNode("C1", 130, 260)
        c2 = TreeNode("C2", 370, 260)
        c3 = TreeNode("C3", 580, 260)
        c4 = TreeNode("C4", 820, 260)
        b1.children = [c1, c2]
        b2.children = [c3, c4]

        # Layer 4: (Depth 4)
        d1 = TreeNode("D1", 70, 380)
        d2 = TreeNode("D2", 190, 380)
        d3 = TreeNode("D3", 310, 380)
        d4 = TreeNode("D4", 430, 380)
        d5 = TreeNode("D5", 640, 380)
        c1.children = [d1, d2]
        c2.children = [d3, d4]
        c3.children = [d5]  # Leaving asymmetry 

        # Layer 5: (Depth 5)
        e1 = TreeNode("E1", 70, 500)
        e2 = TreeNode("E2", 430, 500)
        d1.children = [e1]
        d4.children = [e2]
        
        # Total Nodes count = 1(Root) + 2(B) + 4(C) + 5(D) + 2(E) = 14 nodes.
        # Let's add one more node to make it exactly 15 nodes total.
        e3 = TreeNode("E3", 640, 500)
        d5.children = [e3]

    def create_widgets(self):
        # --- Upper Control Bar ---
        control_frame = tk.Frame(self.root, bg='#252538', pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(
            control_frame, text="Enter Target Node Name (e.g., E2, C3, D1):", 
            font=('Arial', 11, 'bold'), bg='#252538', fg='white'
        ).pack(side=tk.LEFT, padx=(20, 5))

        self.entry_target = tk.Entry(control_frame, font=('Arial', 12), width=8, bg='#121214', fg='white', insertbackground='white')
        self.entry_target.pack(side=tk.LEFT, padx=5)
        self.entry_target.insert(0, "E2") # Default search goal text

        search_btn = tk.Button(
            control_frame, text="🔍 Search Node (Backtrack)", font=('Arial', 11, 'bold'),
            bg='#00E676', fg='black', command=self.start_backtrack_search, relief=tk.FLAT
        )
        search_btn.pack(side=tk.LEFT, padx=15)

        reset_btn = tk.Button(
            control_frame, text="🔄 Reset Dashboard View", font=('Arial', 11),
            bg='#37474F', fg='white', command=self.reset_display, relief=tk.FLAT
        )
        reset_btn.pack(side=tk.LEFT)

        # --- Tree Rendering Canvas ---
        self.canvas = tk.Canvas(self.root, bg='#121214', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.draw_tree(self.root_node)

    def draw_tree(self, node):
        """Recursively renders connections and circle nodes to the graphics viewport."""
        for child in node.children:
            # Draw structural links
            color = '#37474F'
            # Highlight edge if both parent and child are on the active search path
            if node in self.path_taken and child in self.path_taken:
                color = '#00E676' # Neon green connection path
            elif node in self.visited_nodes and child in self.visited_nodes:
                color = '#D32F2F' # Dull crimson path for rejected configurations
                
            self.canvas.create_line(node.x, node.y, child.x, child.y, width=3, fill=color)
            self.draw_tree(child)

        # Render current node node body
        fill_color = '#263238'
        outline_color = '#78909C'
        
        if node in self.path_taken:
            fill_color = '#00E676'  # Green if actively on the solution path
            outline_color = '#FFFFFF'
        elif node.name in self.visited_nodes:
            fill_color = '#D32F2F'  # Red if it was a dead-end and we backtracked off it

        self.canvas.create_oval(node.x-22, node.y-22, node.x+22, node.y+22, fill=fill_color, outline=outline_color, width=2)
        text_color = 'white' if fill_color != '#00E676' else 'black'
        self.canvas.create_text(node.x, node.y, text=node.name, font=('Arial', 10, 'bold'), fill=text_color)

    # --- Core Backtracking Algorithm ---
    def backtrack_search(self, current_node):
        # 1. Update UI state to show node entry
        self.path_taken.append(current_node)
        self.visited_nodes.add(current_node.name)
        
        self.refresh_canvas_view(250) # short execution pause to animate search

        # Base Case / Goal Test Success Check
        if current_node.name.upper() == self.search_target:
            return True

        # 2. Iterate through choices (Child branches)
        for child in current_node.children:
            # Recurse down the branch
            if self.backtrack_search(child):
                return True # Success propagation upward

        # 3. BACKTRACK STEP: If children did not find the target, this path is a dead end.
        # We pop the node off our active solution stack to step back up to the parent.
        self.path_taken.pop()
        self.refresh_canvas_view(250) # short execution pause to animate backtracking
        
        return False

    def start_backtrack_search(self):
        self.search_target = self.entry_target.get().strip().upper()
        self.path_taken = []
        self.visited_nodes.clear()
        
        if not self.search_target:
            messagebox.showwarning("Input Error", "Please provide a valid node key target.")
            return

        found = self.backtrack_search(self.root_node)

        if found:
            path_str = " -> ".join([node.name for node in self.path_taken])
            messagebox.showinfo("Target Found!", f"Successfully located node {self.search_target}!\n\nBacktracked Verification Path:\n{path_str}")
        else:
            messagebox.showerror("Not Found", f"Node '{self.search_target}' does not exist inside this tree topology structure.")

    def refresh_canvas_view(self, ms_delay):
        self.canvas.delete("all")
        self.draw_tree(self.root_node)
        self.root.update()
        self.root.after(ms_delay)

    def reset_display(self):
        self.path_taken.clear()
        self.visited_nodes.clear()
        self.canvas.delete("all")
        self.draw_tree(self.root_node)


if __name__ == "__main__":
    main_window = tk.Tk()
    app = TreeBacktrackDashboard(main_window)
    main_window.mainloop()