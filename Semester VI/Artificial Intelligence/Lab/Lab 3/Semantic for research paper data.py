import random
import json

print(" Step 1: Synthesizing interconnected 30-Paper Research Network...")

# Define structural metadata pools
domains = {
    "CV": ("Computer Vision", "Visual intelligence and spatial feature processing."),
    "NLP": ("Natural Language Processing", "Computational linguistics and sequential text parsing."),
    "Graph_AI": ("Geometric Deep Learning", "Graph-structured data processing and non-Euclidean analytics.")
}

methodologies = {
    "Transformers": ("Transformer Architectures", "Self-attention mechanisms optimized for parallel sequence modeling."),
    "CNNs": ("Convolutional Neural Networks", "Mathematical weight-sharing kernels optimized for spatial grid arrays."),
    "GNNs": ("Graph Neural Networks", "Message-passing node-state configurations optimized for relational topologies."),
    "CL": ("Contrastive Learning", "Self-supervised vector alignment maximizing mutual information across positive pairs.")
}

authors = ["Dr_Y_Bengio", "Dr_G_Hinton", "Dr_Y_LeCun", "Dr_A_Vaswani", "Dr_J_Leskovec"]

# Generate 30 contextual research paper titles distributed across domains
paper_titles = [
    # Computer Vision Papers (1-10)
    ("ResNet-3D: Residual Grids for Spatial Volumetric Analysis", "CV", "CNNs", "Dr_Y_LeCun"),
    ("ViT-Scale: Scaling Vision Transformers for Dense Prediction", "CV", "Transformers", "Dr_A_Vaswani"),
    ("SimCLR-V3: Contrastive Frameworks for Self-Supervised Vision", "CV", "CL", "Dr_G_Hinton"),
    ("Masked Autoencoders Are Scalable Vision Visualizers", "CV", "Transformers", "Dr_Y_LeCun"),
    ("NeRF-Graph: Neural Radiance Fields on Graph Topologies", "CV", "GNNs", "Dr_J_Leskovec"),
    ("Real-Time Semantic Segmentation via Dilated Spatial Kernels", "CV", "CNNs", "Dr_Y_LeCun"),
    ("Cross-Modal Vector Alignment in Generative Vision Spaces", "CV", "CL", "Dr_G_Hinton"),
    ("Attention-Driven Object Detection in High-Resolution Imagery", "CV", "Transformers", "Dr_A_Vaswani"),
    ("Unsupervised Visual Representation via Contrastive Residuals", "CV", "CL", "Dr_G_Hinton"),
    ("Geometry-Aware Convolutions for 3D Point Cloud Processing", "CV", "CNNs", "Dr_J_Leskovec"),
    
    # NLP Papers (11-20)
    ("BERT-Large: Pre-training of Deep Bidirectional Transformers", "NLP", "Transformers", "Dr_A_Vaswani"),
    ("GPT-Next: Autoregressive Language Modeling at Scale", "NLP", "Transformers", "Dr_A_Vaswani"),
    ("Contrastive Sentence Embeddings via Semantic Invariance", "NLP", "CL", "Dr_Y_Bengio"),
    ("Long-Short Sequence Parsing via Linear Attention Windows", "NLP", "Transformers", "Dr_A_Vaswani"),
    ("Text-Graph Recurrent Transformers for Structured Document Analysis", "NLP", "GNNs", "Dr_J_Leskovec"),
    ("Exploring the Limits of Self-Supervised Machine Translation", "NLP", "CL", "Dr_Y_Bengio"),
    ("Dependency-Parsing Convolutions for Low-Resource Languages", "NLP", "CNNs", "Dr_Y_LeCun"),
    ("Token-Free Language Representations via Character-Level Processing", "NLP", "Transformers", "Dr_Y_Bengio"),
    ("Retrieval-Augmented Transformers for Dynamic Knowledge Graphs", "NLP", "Transformers", "Dr_J_Leskovec"),
    ("Evaluating Prompt Calibration Metrics in LLM Quantization", "NLP", "Transformers", "Dr_Y_Bengio"),

    # Graph AI Papers (21-30)
    ("GCN-V2: Scalable Graph Convolutional Networks via Node Sampling", "Graph_AI", "GNNs", "Dr_J_Leskovec"),
    ("Graph Attention Networks with Multi-Head Structural Alignment", "Graph_AI", "Transformers", "Dr_A_Vaswani"),
    ("Self-Supervised Graph Contrastive Learning via Subgraph Masking", "Graph_AI", "CL", "Dr_Y_Bengio"),
    ("Message-Passing Frameworks for Heterogeneous Molecular Topologies", "Graph_AI", "GNNs", "Dr_G_Hinton"),
    ("Graph Convolutions Meet Vision Transformers: A Unified Review", "Graph_AI", "Transformers", "Dr_Y_LeCun"),
    ("Temporal Graph Networks for Dynamic Relational Interaction Stream", "Graph_AI", "GNNs", "Dr_J_Leskovec"),
    ("Inductive Representation Learning on Large-Scale Social Webs", "Graph_AI", "GNNs", "Dr_J_Leskovec"),
    ("Contrastive Node Clustering via Graph Diffusion Wavelets", "Graph_AI", "CL", "Dr_G_Hinton"),
    ("Deep Generative Models for Graph Structure Deconvolution", "Graph_AI", "CNNs", "Dr_Y_LeCun"),
    ("Scalable Graph Neural Architecture Search via Gradient Descent", "Graph_AI", "GNNs", "Dr_Y_Bengio")
]

nodes_dict = {}
edges_set = set()

# Process Domain Metadata Nodes
for dom_key, (dom_name, dom_desc) in domains.items():
    nodes_dict[dom_name] = {
        "group": "Domain", 
        "category": "Academic Field", 
        "rec": "Review literature cross-sections to find multi-disciplinary opportunities."
    }

# Process Methodology Metadata Nodes
for meth_key, (meth_name, meth_desc) in methodologies.items():
    nodes_dict[meth_name] = {
        "group": "Methodology", 
        "category": "Core Algorithm", 
        "rec": f"Lab deployment vector: Isolate this framework to benchmark operational runtime bottlenecks."
    }

# Process Author Metadata Nodes
for author in authors:
    nodes_dict[author] = {
        "group": "Author", 
        "category": "Principal Investigator", 
        "rec": "Analyze h-index and structural degree co-authorship paths to optimize grant sourcing."
    }

# Process the 30 Research Papers into Nodes and Map Structural Affiliation Edges
for idx, (title, dom_key, meth_key, author) in enumerate(paper_titles):
    dom_name = domains[dom_key][0]
    meth_name = methodologies[meth_key][0]
    
    nodes_dict[title] = {
        "group": "Paper",
        "category": f"Published under {dom_name}",
        "rec": f"Literature Mapping Blueprint: Verify citation weights to evaluate the foundational novelty of this work."
    }
    
    # Establish Metadata Semantic Edges
    edges_set.add((title, dom_name, "BELONGS_TO"))
    edges_set.add((title, meth_name, "UTILIZED"))
    edges_set.add((author, title, "AUTHORED"))

# Generate Dense Multi-Layer Internal Citations (Ensures Interconnectedness)
# Lower indices represent older foundational papers, higher indices represent newer works
for i in range(5, len(paper_titles)):
    current_title = paper_titles[i][0]
    current_dom = paper_titles[i][1]
    
    # Target older papers to simulate real retrospective academic referencing
    possible_citations = paper_titles[:i]
    
    # Strategy: High probability to cite papers within the same domain, lower probability to cross domains
    same_domain_pool = [p[0] for p in possible_citations if p[1] == current_dom]
    cross_domain_pool = [p[0] for p in possible_citations if p[1] != current_dom]
    
    citations_to_add = []
    if same_domain_pool:
        citations_to_add.extend(random.sample(same_domain_pool, k=min(len(same_domain_pool), random.randint(1, 3))))
    if cross_domain_pool and random.random() > 0.6:  # 40% chance of cross-pollination
        citations_to_add.append(random.choice(cross_domain_pool))
        
    for cited_paper in citations_to_add:
        if current_title != cited_paper:
            edges_set.add((current_title, cited_paper, "CITES"))

# Format JSON structural layout for WebGL engine
json_data = {
    "nodes": [{"id": name, "group": meta["group"], "category": meta["category"], "rec": meta["rec"]} for name, meta in nodes_dict.items()],
    "links": [{"source": src, "target": tgt, "label": rel} for src, tgt, rel in edges_set]
}

with open("network_data.json", "w") as f:
    json.dump(json_data, f, indent=4)

print(f"✅ Literature Citation Network mapped successfully! Calculated {len(nodes_dict)} nodes and {len(edges_set)}structural paths.")