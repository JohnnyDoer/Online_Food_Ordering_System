from haystack import indexes
from .models import Restaurant, FoodCategory, Food


class FoodIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Food
        excludes = ['Food_ID', 'Food_Pic', 'Food_Discount', 'Food_Price']

    def get_model(self):
        return Food

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
