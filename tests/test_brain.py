######################################################################
#  Q U I Z   B R A I N   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest
from unittest import mock
from quiz_brain import QuizBrain
from .factories import QuestionFactory


class TestQuizBrain(unittest.TestCase):
    """Test Cases for Quiz Brain"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        pass

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        pass

    def setUp(self):
        """This runs before each test"""
        pass

    def tearDown(self):
        """This runs after each test"""
        pass

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_next_question(self):
        """Test next question"""
        # question data from QuestionFactory
        question_data = [QuestionFactory() for _ in range(10)]

        # create QuizBrain
        quiz_brain = QuizBrain(question_data)

        # test next_question
        for _ in range(10):
            with mock.patch("builtins.input", return_value="True"):
                quiz_brain.next_question()

        # test score
        self.assertEqual(quiz_brain.question_number, 10)

    def test_get_current_question(self):
        """Test get current question"""
        # question data from QuestionFactory
        question_data = [QuestionFactory() for _ in range(1)]

        # create QuizBrain
        quiz_brain = QuizBrain(question_data)

        # test score
        self.assertEqual(quiz_brain.get_current_question(), question_data[0])

    def test_still_has_questions(self):
        """Test still has questions"""
        # question data from QuestionFactory
        question_data = [QuestionFactory() for _ in range(10)]

        # create QuizBrain
        quiz_brain = QuizBrain(question_data)

        # test still_has_questions
        for _ in range(10):
            self.assertTrue(quiz_brain.still_has_questions())
            with mock.patch("builtins.input", return_value="True"):
                quiz_brain.next_question()

        # test score
        self.assertFalse(quiz_brain.still_has_questions())

    def test_check_answer(self):
        """Test check answer"""
        # question data from QuestionFactory
        question_data = [QuestionFactory() for _ in range(10)]

        # create QuizBrain
        quiz_brain = QuizBrain(question_data)

        # test check_answer
        current_question = quiz_brain.get_current_question()

        for _ in range(10):

            with mock.patch("builtins.input", return_value="True"):
                quiz_brain.next_question()

                if current_question.answer == "True":
                    self.assertEqual(quiz_brain.check_answer("True", current_question.answer), True)
                else:
                    self.assertEqual(quiz_brain.check_answer("True", current_question.answer), False)

        # test question_number
        self.assertEqual(quiz_brain.question_number, 10)
