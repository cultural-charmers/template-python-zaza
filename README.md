Using template to create a Zaza enabled, classic charm
===========================================

1) Clone template:
------------------

```
sudo apt -y install cookiecutter
cookiecutter https://github.com/cultural-charmers/template-python-zaza.git
```

2) Edit src/config.yaml
-----------------------

- In the src/config.yaml add any options that should be configurable by the
  user.
 
3) Update unit tests
--------------------

Edit unit\_tests/test\_lib\_charm\_\* and update unit
tests.

4) Update functional tests
--------------------------

Update the bundles in tests/bundles/\*yaml as needed and edit
tests\/tests\_\*py to add functional testing.

TODO:
-----
- Add basic zaza tests
- Add unit tests
  * Add skeleton readme for generated charm
