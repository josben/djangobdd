# encoding: utf-8

from behave import given, when, then

@given(u'que ingreso al sistema con el url "{url}"')
def impl(context, url):
    br = context.browser
    br.visit(url)

@given(u'voy a la opcion "{option}"')
def impl(context, option):
    link = context.browser.find_link_by_text(option).first
    assert link
    link.click()

@given(u'empiezo introduciendo el nombre {nombre}')
def step_impl(context, nombre):
    context.browser.fill('name', nombre)
    context.name = nombre
    assert nombre

@given(u'el apellido {apellido}')
def step_impl(context, apellido):
    context.browser.fill('lastname', apellido)
    context.lastname = apellido
    assert apellido

@given(u'algo acerca de el {about}')
def step_impl(context, about):
    context.browser.fill('about', about)
    context.about = about
    assert about

@when(u'oprima el boton {button}')
def step_impl(context, button):
    button = context.browser.find_by_value(button).first
    assert button
    button.click()

@then(u'registro la persona en el sistema')
def step_impl(context):
    assert "Lista de personas registradas" in context.browser.html

