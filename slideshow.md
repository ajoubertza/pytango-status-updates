name: empty layout
layout: true

---
name: title
class: center, middle

PyTango Status Report 
=====================

[Anton Joubert](https://github.com/ajoubertza) ([SARAO](https://sarao.ac.za))

Tango 2020 November status update meeting

Tuesday, 17 November 2020

*

GitHub: [ajoubertza/pytango-status-updates](https://github.com/ajoubertza/pytango-status-updates)

Slides: [https://ajoubertza.github.io/pytango-status-updates/](https://ajoubertza.github.io/pytango-status-updates/)

.centre[<img src="images/nrf_sarao_meerkat_tango.png" height="220">]

---

name: presentation
layout: true
class: middle

PyTango?  Quick reminder
========================

---

- Python library

- Binding over the C++ Tango library

- ... using boost-python (future:  pybind11)

- Relies on numpy

- Multi OS: Linux, Windows, Mac (with Docker...)

- Works on Python 2.7, 3.5, 3.6, 3.7, 3.8, (probably 3.9)

.center[<img src="images/pytango_sw_stack.png" width="400">]

---

name: releases
layout: true
class: middle

Current release - 9.3.2
==============

---

###  May 2020

- `MultiDeviceTestContext`

- `EnsureOmniThread`

- Packages:
  - Source on PyPI (works for Linux)
  
  - Windows wheels on PyPI:  9.3.2 broken! (use 9.3.1)
  
  - Conda Linux binary (pytango on `tango-controls` channel)

---

name: upcoming
layout: true
class: middle

Upcoming release - 9.3.3
========================

---

### Bugfixes

- Fix convert2array for Unicode to DevVarStringArray (Py3) ([#360](https://github.com/tango-controls/pytango/pull/360))

- Fix DeviceProxy repr/str memory leak ([#386](https://github.com/tango-controls/pytango/pull/386))

- _WIP:  Fix Windows binary wheels? ([#367](https://github.com/tango-controls/pytango/issues/367))_

- _WIP:  Fix read/write/is_allowed not called for dynamic attribute in async mode server? ([#337](https://github.com/tango-controls/pytango/pull/337))_


### Features/Changes

- Preserve cause of exception when getting/setting attribute in DeviceProxy ([#365](https://github.com/tango-controls/pytango/pull/365))

- Improve mandatory + default device property error message ([#385](https://github.com/tango-controls/pytango/pull/385))

---

### CI improvements

- CI includes Python 3.8 ([#344](https://github.com/tango-controls/pytango/pull/344))

- CI updated cppTango version 9.3.4rc6 => 9.3.4 ([#389](https://github.com/tango-controls/pytango/pull/389))

- CI under Windows and dev containers updated to boost 1.73.0 ([#376](https://github.com/tango-controls/pytango/pull/376))

- _WIP:  CI runs test suite on Windows - ([#369](https://github.com/tango-controls/pytango/issues/369))_

---

### Development/Testing improvements

- VScode remote development container support ([#377](https://github.com/tango-controls/pytango/pull/377))

- Add string support for MultiDeviceTestContext `devices_info` class field ([#378](https://github.com/tango-controls/pytango/pull/378))

- Add test context support for memorized attributes ([#384](https://github.com/tango-controls/pytango/pull/384))

- _WIP:  Enable short-name access to `TestContext` devices ([#388](https://github.com/tango-controls/pytango/pull/388))_

  _(was "`DeviceProxy` support for `TANGO_HOST` with `#dbase=no`", but no longer using `TANGO_HOST` variable)_

---

### Not included

- Support forwarded attributes with `TestContext` devices (requires cppTango [#796](https://github.com/tango-controls/cppTango/issues/796)).

### Contributors - thanks!

DrewDevereux, ldoyle, reszelaz, stanislaw55, spirit1317, woutdenolf, wkitka


### When can I get it?

- Aiming for December 2020

---

name: issues
layout: true
class: middle

Issues
======

---

### Further investigation required

- DS hangs when concurrently subscribing to events and destructing DeviceProxy ([#315](https://github.com/tango-controls/pytango/issues/315))

- Event-subscribed client segfaults if events cannot reach it ([#371](https://github.com/tango-controls/pytango/issues/371))

- Tango client hangs when it holds stateless event subscription which constantly fails and meanwhile destroys AttributeProxy ([#302](https://github.com/tango-controls/pytango/issues/302))

- Cleanup not performed on SIGINT/SIGTERM if thread is started before call to `tango.server.run` ([#306](https://github.com/tango-controls/pytango/issues/306))

---

name: compatibility
layout: true
class: middle

Compatibility Roadmap
=============

---

### PyTango and cppTango

Currently, match _major.minor_ releases when compiling PyTango binding.

cppTango 9.3.x and 9.4.x not Application Binary Interface (ABI) compatible.

Planned compatibility:
```
         cppTango | PyTango | Works?
        ----------|---------|-------
            9.3.x |   9.3.x | yes
            9.3.x |   9.4.x | probably*
            9.4.x |   9.4.x | yes
```

_* Tested alpha release of cppTango 9.4.x with PyTango 9.3.x.
Tests passed, with only change: `libtango.so.9` ->`libtango.so.94`._

---

name: pybind11
layout: true
class: middle

pybind11
======

---

### Current status

- Code is on pytango [pybind11](https://github.com/tango-controls/pytango/tree/pybind11) branch.

- pybind11 branch and develop (main) branch have diverged significantly.  Need to merge in, or rebase on, develop.

---

### Functionality

Using new tests with device server running outside test suite:
- ✅ device data
- ✅ commands
- ✅ database
- ✅ attribute proxy
- ✅ device proxy
- ✅ pipes
- ✅ pipe events
- ✅ exceptions
- __ push events
- __ callbacks
- __ forward attributes
- __ groups
- __ enums

---

### PyTango standard test suite

Results:

```
            Type of tests | # Failed | # Passed
            --------------|----------|---------
            Client        |       56 |     588 
            Server        |      222 |       4 
            Events        |       20 |       0 
            Async         |       21 |       0 
            Test Context  |       30 |       6 
```

Most failures due to crash for any use of `DeviceTestContext`.

---

name: development
layout: true
class: middle

PyTango development
===================

---

### Hosting

- Repo: [github.com/tango-controls/pytango](https://github.com/tango-controls/pytango)

- Docs: [pytango.readthedocs.io](https://pytango.readthedocs.io)

- Continuous Integration:  TravisCI (Conda on Ubuntu VM).

- Windows packages:  AppVeyor

- Anyone want to migrate us to GitHub Actions instead?

### Issues

- Specific issues:  report on [GitHub](https://github.com/tango-controls/pytango/issues) - the more detail the better

- Questions:  use the [TANGO Forum](https://www.tango-controls.org/community/forum/c/development/python)

---

### Contributing

- Please join in!

- Typical branched Git workflow.  Main branch is `develop`

- Fork the repo, make it better, make a PR.  Thanks!

- More info in [how-to-contribute](https://pytango.readthedocs.io/en/latest/how-to-contribute.html).

---
name:  done
class: center, middle
layout: true

Done!  Any questions?
=====================

GitHub: [ajoubertza/pytango-status-updates](https://github.com/ajoubertza/pytango-status-updates)

Slides: [https://ajoubertza.github.io/pytango-status-updates/](https://ajoubertza.github.io/pytango-status-updates/)

.centre[<img src="images/tango_controls_logo.png" height="120">]
---
