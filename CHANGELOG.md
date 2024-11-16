# Changelog

## [3.0.0](https://github.com/miloth/catppuccin-python/compare/v2.3.4...v3.0.0) (2024-11-16)


### ⚠ BREAKING CHANGES

* change palette data structure to match json, add codegen ([#29](https://github.com/miloth/catppuccin-python/issues/29))

### Features

* Add from hex method ([bef684a](https://github.com/miloth/catppuccin-python/commit/bef684afd4134c417b8b92afdeb625eaeb7f99ec))
* add gh-pages build script for pygments css ([#33](https://github.com/miloth/catppuccin-python/issues/33)) ([7e4584b](https://github.com/miloth/catppuccin-python/commit/7e4584b0365970290d33aa91eff6ef3d87ca43f7))
* add hsl/hsla properties to colours ([#21](https://github.com/miloth/catppuccin-python/issues/21)) ([65113e6](https://github.com/miloth/catppuccin-python/commit/65113e658e9f11a7019e4d04cd3e9f8bbe77b398))
* add identifier field to Color and Flavor ([#32](https://github.com/miloth/catppuccin-python/issues/32)) ([465e326](https://github.com/miloth/catppuccin-python/commit/465e3269e943d2ae492069f7ecedb6ce9799e0fa))
* add iteration over Palette and FlavorColors ([#30](https://github.com/miloth/catppuccin-python/issues/30)) ([411e2df](https://github.com/miloth/catppuccin-python/commit/411e2dfbdcb3afec434d3e698b1cae3f1b775a9a))
* add name field for each flavour ([#20](https://github.com/miloth/catppuccin-python/issues/20)) ([fbdac64](https://github.com/miloth/catppuccin-python/commit/fbdac6446c70168e03838c61cc162d1892779380)), closes [#19](https://github.com/miloth/catppuccin-python/issues/19)
* add opacity to colours ([4f9dae0](https://github.com/miloth/catppuccin-python/commit/4f9dae019c2ecd83d18284811a760d514f77b504))
* add pygments plugins ([32239ce](https://github.com/miloth/catppuccin-python/commit/32239ce685c109f40af78babcfb8a0c5a028c86f))
* add python package ([0f152ea](https://github.com/miloth/catppuccin-python/commit/0f152eac19884f8f4bdb706328d5b3ec7dfb19cc))
* add rich integration ([#17](https://github.com/miloth/catppuccin-python/issues/17)) ([0d3b1db](https://github.com/miloth/catppuccin-python/commit/0d3b1db2a7e8f5c3778c55b65862b25639e7ef9d))
* added `matplotlib` support ([#36](https://github.com/miloth/catppuccin-python/issues/36)) ([580dabc](https://github.com/miloth/catppuccin-python/commit/580dabc3e3c15d9e3043430c100fb867f9847614))
* change palette data structure to match json, add codegen ([#29](https://github.com/miloth/catppuccin-python/issues/29)) ([8695144](https://github.com/miloth/catppuccin-python/commit/8695144d6c8a80049ddbfcff280c04b1145681f8))
* change prefix on pygments css file names ([cfb2694](https://github.com/miloth/catppuccin-python/commit/cfb2694be1a885180744fd3f99e1dba79935d4dc))
* **css:** add important stylesheet variants ([a0fd5b0](https://github.com/miloth/catppuccin-python/commit/a0fd5b0e9db38fe45fbc7364f10ff92966bb8914))
* **css:** scope token classes to `pre` elements ([6c746c1](https://github.com/miloth/catppuccin-python/commit/6c746c1ca7e3aa56ec970f13e76b7381c32165db))
* **css:** target `pre[lang]` in addition to `pre` ([a8eb6b9](https://github.com/miloth/catppuccin-python/commit/a8eb6b994bbbfde1d0839599400601c64b5f17eb))
* Improvements to pygments styles ([#18](https://github.com/miloth/catppuccin-python/issues/18)) ([36cddb8](https://github.com/miloth/catppuccin-python/commit/36cddb80b214bd560110231b45e589a5b20ba6c7))
* **pygments:** "can't you just..." - [@nullishamy](https://github.com/nullishamy) ([#88](https://github.com/miloth/catppuccin-python/issues/88)) ([0e0a289](https://github.com/miloth/catppuccin-python/commit/0e0a2898e7a6e642811f9d8263a4f43d7f0cc035))
* **pygments:** remove line-height ([#86](https://github.com/miloth/catppuccin-python/issues/86)) ([368c755](https://github.com/miloth/catppuccin-python/commit/368c7552dbec69d71b21e68f0d403ff38e68707a))
* refactor and add pygments integration ([6c1d248](https://github.com/miloth/catppuccin-python/commit/6c1d24818fa6c1eaae7e4ef1dc8bac496347a331))


### Bug Fixes

* `.` → `-` ([ef18bd7](https://github.com/miloth/catppuccin-python/commit/ef18bd706b053f02b02067f28de756427efd4a3a))
* add missing feature flag in ci ([91d0d0b](https://github.com/miloth/catppuccin-python/commit/91d0d0b8b61614a3a4af58280900b5315362d6b8))
* **deps:** update dependency matplotlib to v3.9.1 ([#56](https://github.com/miloth/catppuccin-python/issues/56)) ([ed3cc08](https://github.com/miloth/catppuccin-python/commit/ed3cc0849fec8948b3beed8bebce3d3387b198d0))
* **deps:** update dependency matplotlib to v3.9.2 ([#68](https://github.com/miloth/catppuccin-python/issues/68)) ([0d31bdb](https://github.com/miloth/catppuccin-python/commit/0d31bdbacaa5dc80073c317dd5105f6234f8016b))
* **deps:** update dependency pygments to v2.18.0 ([#44](https://github.com/miloth/catppuccin-python/issues/44)) ([b40036e](https://github.com/miloth/catppuccin-python/commit/b40036e78929b965a90fabc728ea7da4e8e2beeb))
* **deps:** update dependency rich to v13.7.1 ([#39](https://github.com/miloth/catppuccin-python/issues/39)) ([f72ae06](https://github.com/miloth/catppuccin-python/commit/f72ae06336b0173fa525d2f93843216e87628673))
* **deps:** update dependency rich to v13.8.0 ([#71](https://github.com/miloth/catppuccin-python/issues/71)) ([9f4ed60](https://github.com/miloth/catppuccin-python/commit/9f4ed60a81b316b2941f372669557b499f7a173f))
* **deps:** update dependency rich to v13.9.2 ([#83](https://github.com/miloth/catppuccin-python/issues/83)) ([73fc25e](https://github.com/miloth/catppuccin-python/commit/73fc25eef69f0188fc26f1814ce9793d63000556))
* **deps:** update dependency tinycss2 to v1.3.0 ([#45](https://github.com/miloth/catppuccin-python/issues/45)) ([c1e9d90](https://github.com/miloth/catppuccin-python/commit/c1e9d90229684944126abdaa8dac226625ec583e))
* **extras/pygments:** align syntax highlighting tokens with style guide ([#75](https://github.com/miloth/catppuccin-python/issues/75)) ([2d0df3d](https://github.com/miloth/catppuccin-python/commit/2d0df3d746a9f6797c9e7b095cdf58ee41f56c72))
* **extras/pygments:** change `Keyword.Reserved` from `pink` to `mauve` ([c0c3ee9](https://github.com/miloth/catppuccin-python/commit/c0c3ee990e5a36150f233ef61f1bae8cd4d09a59))
* **extras/pygments:** change `Name.Exception` from `text` to `yellow` ([c0c3ee9](https://github.com/miloth/catppuccin-python/commit/c0c3ee990e5a36150f233ef61f1bae8cd4d09a59))
* **extras/pygments:** change `Name.Tag` from pink to blue ([#77](https://github.com/miloth/catppuccin-python/issues/77)) ([ecf1972](https://github.com/miloth/catppuccin-python/commit/ecf19729cbc53695db1fe3b0d0dfea5e5d84879e))
* Improve pylint score ([54c5c5c](https://github.com/miloth/catppuccin-python/commit/54c5c5c3be6bcfd4e41da78077a97b4fb76d926f))
* legacy type hint syntax ([f5e35d2](https://github.com/miloth/catppuccin-python/commit/f5e35d2db2d7e5f41ebc4e770382f77d873e359c))
* **pygments:** functions should be `blue`, not `sapphire` ([#79](https://github.com/miloth/catppuccin-python/issues/79)) ([0bdf4e0](https://github.com/miloth/catppuccin-python/commit/0bdf4e025e960af010b79374c3a38caf53d372a4))
* **scripts/build-gh-pages:** add `code` selector for pygments styles ([#69](https://github.com/miloth/catppuccin-python/issues/69)) ([6699255](https://github.com/miloth/catppuccin-python/commit/6699255f59669cd044189c55afd141eba39c591a))


### Reverts

* **css:** remove extra `pre[lang]` selector ([#35](https://github.com/miloth/catppuccin-python/issues/35)) ([3fd71d3](https://github.com/miloth/catppuccin-python/commit/3fd71d31409f901a9c8048d57689a681a50baa12))


### Documentation

* add ipython instructions to readme ([bbe9c17](https://github.com/miloth/catppuccin-python/commit/bbe9c172e80bbedf375a4647057c6a0c59d1f22a))
* add pygments usage information ([cdc1644](https://github.com/miloth/catppuccin-python/commit/cdc16445a4b7fa03a419a53c8a850ecefa3756db))
* fix typo in python readme ([d0fa440](https://github.com/miloth/catppuccin-python/commit/d0fa440a3e6da487ba333aa6f3275de2d13d0eba))
* move iterable docstring from Flavor to FlavorColors ([eaa1e45](https://github.com/miloth/catppuccin-python/commit/eaa1e459f64042c51a9fe2d19afb13eb7922cc2d))
* **readme:** add matplotlib contributors to thanks section ([1695f2f](https://github.com/miloth/catppuccin-python/commit/1695f2f47457d677836ba9c91134c7742cbb5981))
* update python readme with better contribution instructions ([d38a29c](https://github.com/miloth/catppuccin-python/commit/d38a29c1343f83bf0010845228ed8e91a161f632))
* use true colors in ipython example config ([#26](https://github.com/miloth/catppuccin-python/issues/26)) ([b7420ca](https://github.com/miloth/catppuccin-python/commit/b7420cad4ce8e1c3bb6d105ed9f9f45084333274))

## [2.3.4](https://github.com/catppuccin/python/compare/v2.3.3...v2.3.4) (2024-09-08)


### Bug Fixes

* **extras/pygments:** change `Keyword.Reserved` from `pink` to `mauve` ([c0c3ee9](https://github.com/catppuccin/python/commit/c0c3ee990e5a36150f233ef61f1bae8cd4d09a59))
* **extras/pygments:** change `Name.Exception` from `text` to `yellow` ([c0c3ee9](https://github.com/catppuccin/python/commit/c0c3ee990e5a36150f233ef61f1bae8cd4d09a59))

## [2.3.3](https://github.com/catppuccin/python/compare/v2.3.2...v2.3.3) (2024-09-08)


### Bug Fixes

* **extras/pygments:** change `Name.Tag` from pink to blue ([#77](https://github.com/catppuccin/python/issues/77)) ([ecf1972](https://github.com/catppuccin/python/commit/ecf19729cbc53695db1fe3b0d0dfea5e5d84879e))
* **pygments:** functions should be `blue`, not `sapphire` ([#79](https://github.com/catppuccin/python/issues/79)) ([0bdf4e0](https://github.com/catppuccin/python/commit/0bdf4e025e960af010b79374c3a38caf53d372a4))

## [2.3.2](https://github.com/catppuccin/python/compare/v2.3.1...v2.3.2) (2024-09-08)


### Bug Fixes

* **extras/pygments:** align syntax highlighting tokens with style guide ([#75](https://github.com/catppuccin/python/issues/75)) ([2d0df3d](https://github.com/catppuccin/python/commit/2d0df3d746a9f6797c9e7b095cdf58ee41f56c72))

## [2.3.1](https://github.com/catppuccin/python/compare/v2.3.0...v2.3.1) (2024-09-04)


### Bug Fixes

* **deps:** update dependency matplotlib to v3.9.1 ([#56](https://github.com/catppuccin/python/issues/56)) ([ed3cc08](https://github.com/catppuccin/python/commit/ed3cc0849fec8948b3beed8bebce3d3387b198d0))
* **deps:** update dependency matplotlib to v3.9.2 ([#68](https://github.com/catppuccin/python/issues/68)) ([0d31bdb](https://github.com/catppuccin/python/commit/0d31bdbacaa5dc80073c317dd5105f6234f8016b))
* **deps:** update dependency rich to v13.8.0 ([#71](https://github.com/catppuccin/python/issues/71)) ([9f4ed60](https://github.com/catppuccin/python/commit/9f4ed60a81b316b2941f372669557b499f7a173f))
* **scripts/build-gh-pages:** add `code` selector for pygments styles ([#69](https://github.com/catppuccin/python/issues/69)) ([6699255](https://github.com/catppuccin/python/commit/6699255f59669cd044189c55afd141eba39c591a))


### Documentation

* move iterable docstring from Flavor to FlavorColors ([eaa1e45](https://github.com/catppuccin/python/commit/eaa1e459f64042c51a9fe2d19afb13eb7922cc2d))
* **readme:** add matplotlib contributors to thanks section ([1695f2f](https://github.com/catppuccin/python/commit/1695f2f47457d677836ba9c91134c7742cbb5981))

## [2.3.0](https://github.com/catppuccin/python/compare/v2.2.0...v2.3.0) (2024-06-18)


### Features

* added `matplotlib` support ([#36](https://github.com/catppuccin/python/issues/36)) ([580dabc](https://github.com/catppuccin/python/commit/580dabc3e3c15d9e3043430c100fb867f9847614))


### Bug Fixes

* **deps:** update dependency pygments to v2.18.0 ([#44](https://github.com/catppuccin/python/issues/44)) ([b40036e](https://github.com/catppuccin/python/commit/b40036e78929b965a90fabc728ea7da4e8e2beeb))
* **deps:** update dependency rich to v13.7.1 ([#39](https://github.com/catppuccin/python/issues/39)) ([f72ae06](https://github.com/catppuccin/python/commit/f72ae06336b0173fa525d2f93843216e87628673))
* **deps:** update dependency tinycss2 to v1.3.0 ([#45](https://github.com/catppuccin/python/issues/45)) ([c1e9d90](https://github.com/catppuccin/python/commit/c1e9d90229684944126abdaa8dac226625ec583e))


### Reverts

* **css:** remove extra `pre[lang]` selector ([#35](https://github.com/catppuccin/python/issues/35)) ([3fd71d3](https://github.com/catppuccin/python/commit/3fd71d31409f901a9c8048d57689a681a50baa12))
