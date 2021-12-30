from datetime import datetime, timedelta, date
import calendar
from django.utils import timezone


from django.db.models import Q, Sum

from django.views.generic.base import TemplateView
from product.models import Product
from input.models import Input
from output.models import Output


class DashboardIndex(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_products'] = Product.objects.all().count()
        context['count_products_active'] = Product.objects.filter(status=True).count()
        context['count_products_no_active'] = Product.objects.filter(status=False).count()
        context['graph_inputs'] = self.graph_inputs()
        context['saldos'] = self.saldos()
        #context['list_values'] = self.list_values(self)

        #self.list_values()

        return context
    

    #def list_values(self):
    #    output = Output.objects.order_by('-created_at')[0]

    #    current_date = datetime.now()
    #    primary_date = date("Y-m-d", datetime.strtotime("-1 month", datetime.strtotime(str(current_date))))

    #    print(current_date, primary_date)

        #for i in range( datetime.now(), timedelta(), -1):
            #print("primeiro do mês", datetime(date, i, 1))
            #print("ultimo do mês", datetime()) calendar.monthrange(2002,1)




    def saldos(self):
        output = Output.objects.all().aggregate(price=Sum('price')).get('price') * Output.objects.all().count()
        input = Input.objects.all().aggregate(price=Sum('price')).get('price') * Input.objects.all().count()
        liquid = output - input

        return {'output': f"{output:.2f}", 'input': f"{input:.2f}", 'liquid': f"{liquid:.2f}" }

    def graph_inputs(self):

        date = timezone.now() + timedelta(days=30)
        month = date.month
        year = date.year
        
        dates = []
        input = []
        output = []
        
        for i in range(6):
            
            input.append(Input.objects.filter(
                    Q(created_at__month=month),
                    Q(created_at__year=year)
                ).aggregate(amount=Sum('amount'), price=Sum('price')))

            output.append(Output.objects.filter(
                    Q(created_at__month=month),
                    Q(created_at__year=year)
                ).aggregate(amount=Sum('amount'), price=Sum('price')))

            input[i]['amount'] = float(input[i]['amount']) if input[i]['amount'] else 0
            input[i]['price'] = float(input[i]['price']) if input[i]['price'] else 0

            output[i]['amount'] = float(output[i]['amount']) if output[i]['amount'] else 0
            output[i]['price'] = float(output[i]['price']) if output[i]['price'] else 0

            if month > 1:
                month = month - 1
            else:
                month = 12
                year = year - 1

            dates.append(f'{month}/{year}')            


        dates.reverse()
        input.reverse()
        output.reverse()

        return {"dates": dates, "input": input, "output": output}

