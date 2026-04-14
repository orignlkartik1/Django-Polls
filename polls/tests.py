from django.test import TestCase
from .models import Question, Choice
from django.urls import reverse

class QuestionModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text="What's new?",
            pub_date=timezone.now()
        )

    def test_question_str(self):
        self.assertEqual(str(self.question), "What's new?")

    def test_was_published_recently_with_future_question(self):
        future_question = Question(
            question_text='Future question',
            pub_date=timezone.now() + datetime.timedelta(days=30)
        )
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        old_question = Question(
            question_text='Old question',
            pub_date=timezone.now() - datetime.timedelta(days=30)
        )
        self.assertIs(old_question.was_published_recently(), False)


class ChoiceModelTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Question for choice',
            pub_date=timezone.now()
        )
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            votes=0
        )

    def test_choice_str(self):
        self.assertEqual(str(self.choice), 'Choice 1')


class IndexViewTests(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Public question',
            pub_date=timezone.now()
        )

    def test_index_view_with_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [self.question])


class VoteViewTests(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            question_text='Test question',
            pub_date=timezone.now()
        )
        self.choice = Choice.objects.create(
            question=self.question,
            choice_text='Test choice',
            votes=0
        )

    def test_vote_increments_choice_votes(self):
        response = self.client.post(reverse('polls:vote', args=(self.choice.id,)))
        self.choice.refresh_from_db()
        self.assertEqual(self.choice.votes, 1)
        self.assertRedirects(response, reverse('polls:index'))
