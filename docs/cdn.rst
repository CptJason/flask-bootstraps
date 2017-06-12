CDN support
===========

Flask-Bootstrap supports delivery via CDN or local resources, configurable at
runtime. Upon initialization, Flask-Bootstrap will store a dictionary on your
app named ``yourapp.extensions['bootstrap']['cdns']``, which maps names to
:py:class:`~flask_bootstraps.CDN` instances.

You can use :py:func:`~flask_bootstraps.bootstrap_find_resource` in your
templates as well when using other resources that may be available on CDNs.
CDNs can be added by adding new entries to the dictionary mention above.

.. autoclass:: flask_bootstraps.CDN
   :members:

.. autoclass:: flask_bootstraps.StaticCDN
   :members:

.. autoclass:: flask_bootstraps.WebCDN
   :members:

.. autofunction:: flask_bootstraps.bootstrap_find_resource
