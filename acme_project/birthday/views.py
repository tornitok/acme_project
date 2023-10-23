# birthday/views.py 
from typing import Any

from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayUpdateView(UpdateView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayDeleteView(DeleteView):
    form_class = BirthdayForm
    model = Birthday


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )

        return context
