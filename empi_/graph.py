import rdflib
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
g = rdflib.Graph()

# Define Namespaces
ex = rdflib.Namespace("http://example.org/inclusive_education#")

# Add Educational Institutions
g.add((ex.University, rdflib.RDF.type, ex.EducationalInstitution))
g.add((ex.School, rdflib.RDF.type, ex.EducationalInstitution))
g.add((ex.NonProfit, rdflib.RDF.type, ex.EducationalInstitution))

# Add Disabilities
g.add((ex.ADHD, rdflib.RDF.type, ex.Disability))
g.add((ex.ASD, rdflib.RDF.type, ex.Disability))
g.add((ex.VisualImpairment, rdflib.RDF.type, ex.Disability))

# Add Accessibility Measures
g.add((ex.WheelchairRamps, rdflib.RDF.type, ex.AccessibilityMeasure))
g.add((ex.BrailleMaterials, rdflib.RDF.type, ex.AccessibilityMeasure))
g.add((ex.AssistiveTechnology, rdflib.RDF.type, ex.AccessibilityMeasure))

# Add Psychological Support
g.add((ex.CounselingServices, rdflib.RDF.type, ex.PsychologicalSupport))
g.add((ex.SupportGroups, rdflib.RDF.type, ex.PsychologicalSupport))
g.add((ex.Therapists, rdflib.RDF.type, ex.PsychologicalSupport))

# Add Educational Practices
g.add((ex.IEP, rdflib.RDF.type, ex.EducationalPractice))
g.add((ex.UDL, rdflib.RDF.type, ex.EducationalPractice))
g.add((ex.CollaborativeLearning, rdflib.RDF.type, ex.EducationalPractice))

# Add Policies
g.add((ex.InclusiveEducationPolicy, rdflib.RDF.type, ex.Policy))
g.add((ex.DisabilityRightsAct, rdflib.RDF.type, ex.Policy))
g.add((ex.EqualAccessPolicy, rdflib.RDF.type, ex.Policy))

# Add Relationships (Edges)
g.add((ex.University, ex.offers, ex.CounselingServices))
g.add((ex.School, ex.provides, ex.WheelchairRamps))
g.add((ex.NonProfit, ex.implements, ex.InclusiveEducationPolicy))
g.add((ex.School, ex.supports, ex.ADHD))
g.add((ex.University, ex.follows, ex.UDL))
g.add((ex.CounselingServices, ex.addresses, ex.ASD))
g.add((ex.InclusiveEducationPolicy, ex.promotes, ex.CollaborativeLearning))

# Convert RDF graph to NetworkX graph for visualization
G_nx = nx.Graph()

# Add nodes and edges to the NetworkX graph
for subj, pred, obj in g:
    G_nx.add_edge(subj.split('#')[-1], obj.split('#')[-1], label=pred.split('#')[-1])

# Set the figure size to make the graph fit the picture
plt.figure(figsize=(12, 14))  # Adjust the figure size as needed

# Draw the graph
pos = nx.spring_layout(G_nx)  # Layout for visualization
edge_labels = nx.get_edge_attributes(G_nx, 'label')
nx.draw(G_nx, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=11, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=edge_labels)

# Display the graph
plt.show()

# Save to graph.xml
g.serialize(format="xml")