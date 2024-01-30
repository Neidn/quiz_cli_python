import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from question_model import Question


class QuestionFactory(factory.Factory):
    """Creates fake questions for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Question

    text = factory.Faker("text")
    answer = FuzzyChoice(choices=["True", "False"])
