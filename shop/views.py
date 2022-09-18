from django.shortcuts import render
from django.views import View

from django.db.models import Q

from .models import Category, Product
from .forms import CategorySearchForm, ProductMaxPriceForm, ProductMinPriceForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        query   = Q()

        if "search" in request.GET:
            search      = request.GET["search"]
            raw_words   = search.replace("　"," ").split(" ")
            words       = [ w for w in raw_words if w != ""]

            for w in words:
                query &= Q(name__contains=w)
        

        form    = CategorySearchForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            # ForeignKeyをバリデーション、clean()して得られる値は、紐づいているモデルオブジェクト。
            query   &= Q(category=cleaned["category"].id)
        
        form        = ProductMaxPriceForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            query   &= Q(price__lte=cleaned["max_price"])

        form        = ProductMinPriceForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            query   &= Q(price__gte=cleaned["min_price"])


        context["products"]     = Product.objects.filter(query).order_by("-dt")
        context["categories"]   = Category.objects.all().order_by("-dt")

        return render(request, "shop/index.html", context)

index = IndexView.as_view()
