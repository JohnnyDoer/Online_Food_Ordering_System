from haystack import indexes

from .models import Restaurant, FoodCategory, Food



class RestaurantIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Restaurant
        excludes = ['Restaurant_ID', 'user', 'Restaurant_Logo', 'Restaurant_Num', 'Restaurant_Email', 'Restaurant_Regex', 'Restaurant_Pin']

    def get_model(self):
        return Restaurant

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class FoodIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Food
        excludes = ['Food_ID', 'Food_Pic', 'Food_Discount', 'Food_Price', 'Restaurant_Email', 'Restaurant_Regex', 'Restaurant_Pin']

    def get_model(self):
        return Food

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

