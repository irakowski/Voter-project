import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from .models import Question, Choice, Category

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions with pub_date
        in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for question that is older
        than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a questions with the given 'question_text' and published the 
    given number of 'days' offset to now(negative for questions published 
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_category(name="Cat1", description="Description1"):
    c = Category.objects.create(name=name, description=description)
    return c

class LandingPageTests(TestCase):
    def test_general_access(self):
        """
        Verifies page loads normally and returns 200 ok on access
        """
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)

    def test_context_data(self):
        """
        If no categories created, an appropriate message is displayed
        """
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No categories created so far. populate_polls_db before lanching an app is required.")
        self.assertQuerysetEqual(response.context['categories'], [])
        
    def test_most_popular_categories(self):
        """
        Verifies Landing page lists the most popular categories in order
        """
        cat1 = create_category()
        q1 = create_question(question_text="Sample question for cat1", days=-2)
        q1.choice_set.create(choice_text="choice1 for q1", votes=15)
        cat2 = create_category(name="Cat2", description="Desc for Cat2")
        q2 = create_question(question_text="Sample question for cat2", days=-2)
        q2.choice_set.create(choice_text="choice1 for q2", votes=4)
        cat1.question.add(q1)
        cat2.question.add(q2)
        response = self.client.get(reverse('landing-page'))
        self.assertQuerysetEqual(response.context['categories'], ['<Category: Cat1>', '<Category: Cat2>'], ordered=False )


class CategoriesViewTests(TestCase):

    def test_all_category_display(self):
        cat1 = create_category()
        q1 = create_question(question_text="Sample question for cat1", days=-2)
        q1.choice_set.create(choice_text="choice1 for q1", votes=15)
        cat2 = create_category(name="Cat2", description="Desc for Cat2")
        q2 = create_question(question_text="Sample question for cat2", days=-2)
        q2.choice_set.create(choice_text="choice1 for q2", votes=4)
        cat1.question.add(q1)
        cat2.question.add(q2)
        cat3 = create_category(name="New Cat3", description="Desc for Cat3")
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['categories']), 3)


class CategoryQuestionViewTests(TestCase):
    """
    Verifies that view displays questions with set choices
    """
    def test_question_display(self):
        cat1 = create_category()
        q1 = create_question(question_text="Sample question1 for cat1", days=-2)
        q1.choice_set.create(choice_text="choice1 for q1", votes=3)
        q2 = create_question(question_text="Sample question2 for cat1", days=-2)
        cat1.question.add(q1, q2)
        response = self.client.get(reverse('polls:category-polls', args=(cat1.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, q1.question_text) 
        self.assertNotIn(response.content, b'Sample question2 for cat1')

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question_with_choice(self):
        """
        Question with a pub_date in the past and choice set are displayed  
        on the index page.
        """
        q = create_question(question_text="Past question.", days=-30)
        q.choice_set.create(choice_text='Answer 1')
        q.choice_set.create(choice_text='Answer 2')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_past_question_with_no_choice(self):
        """
        Question with pub_date in the past and without choice set are not displayed
        on the index page
        """
        create_question(question_text="Past question.", days=-15)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't dispalyed on
        the index page.
        """
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions 
        are displayed.
        """
        q = create_question(question_text='Past question.', days=-30)
        q.choice_set.create(choice_text="Answer 1")
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

    def test_two_past_question_with_choice_set(self):
        """
        The questions index page may display multiple questions.
        """
        q1 = create_question(question_text="Past question 1.", days=-30)
        q1.choice_set.create(choice_text='Answer to q1')
        q2 = create_question(question_text="Past question 2.", days=-5)
        q2.choice_set.create(choice_text='Answer to q2')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        cat = create_category()
        cat.question.add(future_question)
        url = reverse('polls:question-detail', args=(cat.slug, future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question_without_choice(self):
        """
        The detail view of a past question without choice set returns 404 not found
        """
        q = create_question(question_text='Past question', days=-8)
        cat = create_category()
        cat.question.add(q)
        url = reverse('polls:question-detail', args=(cat.slug, q.id ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past AND choice set
        displays the question's text.
        """
        past_question = create_question(question_text='Past question.', days=-5)
        past_question.choice_set.create(choice_text="Answer 1")
        cat = create_category()
        cat.question.add(past_question)
        url = reverse('polls:question-detail', args=(cat.slug, past_question.id ))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class VoteTests(TestCase):
    def test_vote_for_question_without_choice(self):
        """
        Questions without set choice should return 404
        """
        q = create_question(question_text="Question 1.", days=-3)
        cat = create_category()
        cat.question.add(q)
        url = reverse('polls:vote', args=(cat.slug, q.id ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_vote_for_future_question(self):
        """
        Questions that have not been published yet should return 404 not found 
        for voting
        """
        q = create_question(question_text="Some Question", days=4)
        cat = create_category()
        cat.question.add(q)
        url = reverse('polls:vote', args=(cat.slug, q.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_normal_vote(self):
        q = create_question(question_text="Past question.", days=-6)
        cat = create_category()
        cat.question.add(q)
        q.choice_set.create(choice_text="Choice 1 for Past Question.")
        q.choice_set.create(choice_text="Choice 2 for Past Question.")
        url = reverse('polls:vote', args=(cat.slug, q.id ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Choice 1 for Past Question.', response.content)

    def test_post_vote(self):
        q = create_question(question_text="Past question.", days=-6)
        cat = create_category()
        cat.question.add(q)
        c1 = q.choice_set.create(choice_text="Choice 1 for Past Question.")
        c2 = q.choice_set.create(choice_text="Choice 2 for Past Question.")
        url = reverse('polls:vote', args=(cat.slug, q.id, ))
        response = self.client.post(url, {
            'choice': c1.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('polls:question-results', args=(cat.slug, q.id)), status_code=302, target_status_code=200)
    
    def test_vote_no_choice(self):
        q = create_question(question_text="Past question.", days=-6)
        cat = create_category()
        cat.question.add(q)
        c1 = q.choice_set.create(choice_text="Choice 1 for Past Question.")
        c2 = q.choice_set.create(choice_text="Choice 2 for Past Question.")
        url = reverse('polls:vote', args=(cat.slug, q.id, ))
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"You didn&#x27;t select a choice.", response.content)


class QuestionResultViewTests(TestCase):
    def test_result_for_future_test(self):
        """
        Make sure that result page returns 404 for test that haven't been published yet
        """
        q = create_question(question_text="Future question.", days=7)
        q.choice_set.create(choice_text="Choice 1.")
        cat = create_category()
        cat.question.add(q)
        url = reverse('polls:question-results', args=(cat.slug, q.id ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_result_for_question_without_choice(self):
        """
        Result page for question without choices should return 404
        not found
        """
        q = create_question(question_text='Past question.', days=-7)
        cat = create_category()
        cat.question.add(q)
        url = reverse('polls:question-results', args=(cat.slug, q.id ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_result_for_posted_and_voted(self):
        """
        Result page for voted questions should display number of votes
        """
        q = create_question(question_text='Past question.', days=-5)
        cat = create_category()
        cat.question.add(q)
        c = q.choice_set.create(choice_text='Choice 1.')
        self.assertEqual(c.votes, 0)
        url = reverse('polls:vote', args=(cat.slug, q.id ))
        response = self.client.post(url, {'choice': c.id})
        self.assertRedirects(response, expected_url=reverse('polls:question-results', args=(cat.slug, q.id )), status_code=302, target_status_code=200)
        c.refresh_from_db()
        self.assertEqual(c.votes, 1)