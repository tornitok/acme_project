from django.shortcuts import render

from .forms import BirthdayForm


def birthday(request):
    form = BirthdayForm(request.GET or None)
    if form.is_valid:
        pass
#    if request.GET:
        # ...передаём параметры запроса в конструктор класса формы
#        form = BirthdayForm(request.GET)
#
#        if form.is_valid():
#             ...то считаем, сколько дней осталось до дня рождения.
#            Пока функции для подсчёта дней нет — поставим pass:
#            pass

#    else:
        # То просто создаём пустую форму.
#        form = BirthdayForm()

    context = {'form': form}
    return render(request, 'birthday/birthday.html', context=context)
