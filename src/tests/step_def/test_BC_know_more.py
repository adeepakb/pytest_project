from pytest_bdd import scenarios, when

from pages.android.Hamburgermenu import Hamburger

feature_file_name = 'BYJUS CLASSES - Know More option in left navigation'

scenarios('../features/' + feature_file_name + '.feature')




@when('verify that the Left nav is displayed')
def ham_verify(driver):
    Hamburg = Hamburger(driver)
    Hamburg.hamburger_verify(driver)