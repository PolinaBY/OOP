import yaml


class StudentRepYaml(StudentStrategy):
    """Стратегия для работы с YAML."""

    def load(self, file_path: str) -> List[dict]:
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file) or []
        except FileNotFoundError:
            return []

    def save(self, file_path: str, data: List[dict]):
        with open(file_path, 'w') as file:
            yaml.safe_dump(data, file, default_flow_style=False)

    def display(self, file_path: str):
        data = self.load(file_path)
        for item in data:
            print(item)
