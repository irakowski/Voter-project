from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Category, Choice, Question


class LandingPage(generic.TemplateView):
    """
    Landing Page: displays Welcome message and first three categories with questions that got most votes
    """
    template_name = 'polls/landing-page.html'

    def get_context_data(self, **kwargs):
        """
        Passing categories to the context
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first three category
        context['categories'] = Category.objects.annotate(num_votes=Count('question__choice__votes')).order_by('-num_votes')[:3]
        return context


class CategoriesView(generic.ListView):
    """
    List of all Categories
    """
    model = Category
    template_name = 'polls/categories.html'
    context_object_name = 'categories'
       

class CategoryQuestionView(generic.DetailView):
    """
    Displays all questions related to the specific category
    """
    model = Category
    template_name = 'polls/category-questions.html'


class DetailView(generic.DetailView):
    """
    Displays specific question for with choices for voting
    """
    model = Question
    template_name = 'polls/question-detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet and without choices set.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__isnull=True)
    
    def get_context_data(self, **kwargs):
        """
        Passing categories to the context
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first three category
        context['category'] = Category.objects.get(question=self.object)
        return context

def question_vote(request, slug, pk):
    category = get_object_or_404(Category, slug=slug)
    question = get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__isnull=True), category=category.pk, pk=pk)   
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'polls/question-detail.html', {
            'question': question, 
            'category': category,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:question-results', args=(slug, pk)))

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes access to any questions that hasn't been published yet and have no choice set
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__isnull=True)
    
    def get_context_data(self, **kwargs):
        """
        Passing categories to the context
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of first three category
        context['category'] = Category.objects.get(question=self.object)
        return context


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return last five published questions that have choices set
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).exclude(choice__isnull=True).order_by('-pub_date')