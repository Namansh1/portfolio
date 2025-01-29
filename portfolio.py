class Portfolio:
    def __init__(self, name, profession, skills, descriptions):
        self.name = name
        self.profession = profession
        self.skills = skills
        self.descriptions = descriptions

    def display(self):
        print("---------- Portfolio ----------")
        print(f"Name           : {self.name}")
        print(f"Profession     : {self.profession}\n")
        print(f"About {self.name}:\n{self.descriptions['profession']}\n")
        print("Skills         :")
        for skill in self.skills:
            print(f" - {skill}")
        print("\nSkill Details:")
        for skill in self.skills:
            print(f"\n{skill}:\n{self.descriptions[skill]}")
        print("-------------------------------")

# Detailed descriptions
descriptions = {
    "profession": """
    Naman Sharma, an innovative and results-driven AI/ML Engineer, specializes in creating intelligent systems that improve decision-making processes. With a solid foundation in machine learning algorithms, deep learning networks, and data analytics, Naman has successfully led multiple projects that integrate AI technologies to solve complex problems. His passion for advancing the field of artificial intelligence is evident in his contributions to open-source projects and his active participation in AI conferences and workshops.
    """,
    "Graphic Designing": """
    As an expert in graphic designing, Naman Sharma excels in creating visually compelling and cohesive designs that communicate effectively. His proficiency with tools like Adobe Creative Suite, Sketch, and Figma allows him to transform ideas into stunning visuals. Naman's eye for detail and creativity has earned him accolades in various design competitions, and his portfolio showcases a diverse range of projects from branding to user interface design.
    """,
    "Python Programming": """
    An adept Python programmer, Naman Sharma has extensive experience in developing robust and efficient code. His expertise spans a wide array of Python libraries and frameworks, including TensorFlow, PyTorch, pandas, and Django. Naman is particularly skilled in automating tasks, building data-driven applications, and implementing machine learning models. His contributions to Python-based projects are well-recognized in the developer community, and he is often sought after for his ability to write clean, maintainable code.
    """
}

# Creating a portfolio for Naman Sharma
naman_portfolio = Portfolio(
    name="Naman Sharma",
    profession="AI/ML Engineer",
    skills=["Graphic Designing", "Python Programming"],
    descriptions=descriptions
)

# Display the portfolio
naman_portfolio.display()
