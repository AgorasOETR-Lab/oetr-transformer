from src.rotation import rotate_roles
from src.metacognition import metacognitive_function


class OETRModel:
    def __init__(self, roles, heads):
        self.roles = roles
        self.heads = heads

    def process(self, input_data):
        all_outputs = []

        for step in range(len(self.roles)):
            assignments = rotate_roles(self.heads, self.roles, step)

            step_outputs = []
            for head, role in assignments.items():
                output = role.apply(input_data)
                step_outputs.append(output)

            all_outputs.extend(step_outputs)

        meta_output = metacognitive_function(all_outputs)
        return meta_output
      
