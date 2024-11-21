from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from Centr.models import MenuTrainingCent, RecordForm, more_detailed, card_info
from Centr.models import MenuAbout
from Centr.models import Teacher


# Create your views here.
def index(request):
    menu_ppd = MenuTrainingCent.objects.filter(type__exact='PPD').order_by('?')[:3]
    menu_dpd = MenuTrainingCent.objects.filter(type__exact='DPD').order_by('?')[:3]
    context = {'menu_ppd': menu_ppd, 'menu_dpd': menu_dpd}
    return render(
        request,
        'index.html',
        context=context

    )


def about(request):
    menuAb_OsS = MenuAbout.objects.filter(type__exact='OsS')
    menuAb_Dok = MenuAbout.objects.filter(type__exact='Dok')
    menuAb_Obr = MenuAbout.objects.filter(type__exact='Obr')
    menuAb_POU = MenuAbout.objects.filter(type__exact='POU')
    menuAb_RPN = MenuAbout.objects.filter(type__exact='RPN')
    person = Teacher.objects.all()

    context = {'menuAb_OsS': menuAb_OsS, 'menuAb_Dok': menuAb_Dok, 'menuAb_Obr': menuAb_Obr, 'menuAb_POU': menuAb_POU,
               'menuAb_RPN': menuAb_RPN, 'person': person}
    return render(
        request,
        'about.html',
        context=context
    )


def info_program(request,title):
    program = more_detailed.objects.all()  # 'title': titleprogram=program
    # title = program.title
    infa = card_info.objects.all() # filter(program_id), program_id

    context = {'infa': infa, 'program': program,'title':title}
    return render(request, 'card_info.html', context=context,)


def detailed(request, object_id):  # object_id принимает id из URL
    detail = get_object_or_404(MenuTrainingCent, pk=object_id)
    program = more_detailed.objects.order_by('type')
    infa = card_info.objects.all()

    context = {'infa': infa,'detail': detail, 'program': program}
    return render(request, 'more_detailed.html', context=context)


# def detailed(request, object_id):  # object_id принимает id из URL
#     detail = get_object_or_404(MenuTrainingCent, pk=object_id)
#     program = more_detailed.objects.order_by('type')
#     infa = card_info.objects.all()  # Получите все записи из card_info
#
#     # Объединение данных
#     combined_data = []
#     for item in infa:
#         for program_item in program:
#             if item.name == program_item.title:  # Проверка на совпадение name и title
#                 combined_data.append({
#                     'infa': item,
#                     'program': program_item
#                 })
#
#     context = {'detail': detail, 'combined_data': combined_data}
#     return render(request, 'more_detailed.html', context=context)


def contact(request):
    return render(
        request,
        'contact.html',
    )


def record_view(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            # Обработать данные из формы
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            telephone = form.cleaned_data['telephone']
            comment = form.cleaned_data['comment']

            # Отправить данные на email
            subject = 'Новая запись на сайте'
            message = f'Имя: {name}\nПочта: {mail}\nТелефон: {telephone}\nКоментарий: {comment}'
            from_email = 'evgen2712@bk.ru'  # Замените на ваш email
            recipient_list = ['evgen271215@yandex.ru']  # Замените на email получателя

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                print(send_mail)
                return render(request, 'record_success.html')  # Перенаправить на страницу успешной отправки
            except Exception as e:
                # Обработка ошибки отправки почты
                print(send_mail)
                print(f'Ошибка отправки письма: {e}')
                return render(request, 'record_error.html')  # Перенаправить на страницу с сообщением об ошибке

    else:
        form = RecordForm()

    return render(request, 'forms/record_form.html', {'form': form})


def callback_form(request):
    return render(
        request,
        'forms/callback_form.html',
        # Передаем контекст, чтобы форма была доступна в шаблоне
        {'callback_form': callback_form}
    )


def payment_form(request):
    return render(
        request,
        'forms/payment_form.html',
        # Передаем контекст, чтобы форма была доступна в шаблоне
        {'payment_form': payment_form}
    )


def prerpodg_view(request):
    menu_ppd = MenuTrainingCent.objects.filter(type__exact='PPD')

    context = {'menu_ppd': menu_ppd, }
    return render(
        request, 'prerpodg.html',
        context=context)


def dopodgot_view(request):
    menu_dpd = MenuTrainingCent.objects.filter(type__exact='DPD')
    context = {'menu_dpd': menu_dpd}
    return render(
        request, 'dopodgot.html',
        context=context)
