import json

class OntologicalModeler:
    """
    Harari-4C-Protocol: Creativity Module
    Generates structured ontological schemas for complex systems.
    Helps in mapping the 'DNA' of a project for better creativity and expansion.
    """
    
    def __init__(self, system_name):
        self.system_name = system_name
        self.concepts = {}
        self.relations = []

    def add_concept(self, name, attributes):
        self.concepts[name] = attributes

    def add_relation(self, source, target, relationship):
        self.relations.append({
            "from": source,
            "to": target,
            "type": relationship
        })

    def export_ontology(self):
        ontology = {
            "system": self.system_name,
            "concepts": self.concepts,
            "relations": self.relations
        }
        return json.dumps(ontology, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    modeler = OntologicalModeler("Harari-4C-Protocol")
    
    # Adding 4C Concepts
    modeler.add_concept("Critical Thinking", ["Logic", "Bias Detection", "Truth Verification"])
    modeler.add_concept("Communication", ["Clarity", "Prompting", "Symmetry"])
    modeler.add_concept("Collaboration", ["Swarm Intelligence", "Decentralization", "Agile"])
    modeler.add_concept("Creativity", ["Ontology", "Security-by-Design", "Adaptation"])

    # Adding Relations
    modeler.add_relation("Critical Thinking", "Communication", "Filters")
    modeler.add_relation("Communication", "Collaboration", "Enables")
    modeler.add_relation("Creativity", "Critical Thinking", "Inspires New Frameworks")
    modeler.add_relation("Collaboration", "Creativity", "Multiplies Output")

    print("--- Harari-4C: Ontological Model ---")
    print(modeler.export_ontology())
