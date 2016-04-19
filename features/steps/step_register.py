
from behave import given, when, then
from hamcrest import assert_that, equal_to

class RegisterPerson(object):
    def __init__(self, nombre=None, apellido=None, about=None, button=None):
        self.nombre = nombre
        self.apellido = apellido
        self.about = about
        self.button = button

    def save(self):
        assert self.nombre is not None
        assert self.apellido is not None
        assert self.about is not None

        if self.button == 'submit':
            return 'Registro guardado'
        else:
            return 'Error al registrar'

@given(u'que he introducido el nombre {nombre}')
def step_impl(context, nombre):
    context.nombre = nombre

@given(u'el apellido {apellido}')
def step_impl(context, apellido):
    context.apellido = apellido

@given(u'el apellido ')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given el apellido ')

@given(u'algo acerca de el {about}')
def step_impl(context, about):
    context.about = about

@when(u'oprima el boton {button}')
def step_impl(context, button):
    context.button = button
    context.register = RegisterPerson(context.nombre,
                                      context.apellido,
                                      context.about,
                                      context.button)

@then(u'registro la persona en el sistema')
def step_impl(context):
    assert_that('Registro guardado', equal_to(context.register.save()))

