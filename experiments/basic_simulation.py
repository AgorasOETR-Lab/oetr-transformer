from src.roles import Role
from src.oetr_model import OETRModel

roles = [
    Role("Analysis", lambda x: x + 1),
    Role("Synthesis", lambda x: x * 2),
    Role("Evaluation", lambda x: x - 1),
    Role("Context", lambda x: x / 2),
    Role("Abstraction", lambda x: x ** 2),
    Role("Reduction", lambda x: x % 5),
    Role("Comparison", lambda x: x + 3),
    Role("Prediction", lambda x: x * 0.5),
]

heads = [f"H{i}" for i in range(8)]

model = OETRModel(roles, heads)

input_data = 10
output = model.process(input_data)

print("Final Output:", output)
