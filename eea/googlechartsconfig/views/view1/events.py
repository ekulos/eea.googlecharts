""" Handle events
"""
from eea.googlechartsconfig.views.events import facet_deleted

def view1_facet_deleted(obj, evt):
    """ Cleanup removed facet from view properties
    """
    return facet_deleted(obj, evt, 'googlechart.view1')
