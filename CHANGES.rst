ChangeLog
---------

+------------+------------------------------------------------------------------------+------------+
| Version    | Description                                                            | Date       |
+============+========================================================================+============+
| **1.6.1**  | * Trigger publish on github actions                                    | 2022/01/09 |
+------------+------------------------------------------------------------------------+------------+
| **1.6.0**  | * Remove redundant ``ws2812`` package                                  | 2022/01/03 |
+------------+------------------------------------------------------------------------+------------+
| **1.5.0**  | * Drop support for Python 2.7, only 3.5 or newer is supported now      | 2020/07/04 |
+------------+------------------------------------------------------------------------+------------+
| **1.4.1**  | * Make ``contrast`` an optional constructor argument                   | 2019/12/08 |
+------------+------------------------------------------------------------------------+------------+
| **1.4.0**  | * Rework namespace handling for luma sub-projects                      | 2019/06/16 |
+------------+------------------------------------------------------------------------+------------+
| **1.3.1**  | * Fix alpha-channel blending for Unicorn Hat HD display                | 2019/05/26 |
+------------+------------------------------------------------------------------------+------------+
| **1.3.0**  | * Add support for Pimoroni's Unicorn Hat HD                            | 2019/05/26 |
+------------+------------------------------------------------------------------------+------------+
| **1.2.0**  | * Add option to control if 8x8 blocks are arranged in reverse order    | 2019/04/20 |
|            | * Add (approximations of) more characters for 7-segment displa         |            |
|            | * Documentation updates                                                |            |
+------------+------------------------------------------------------------------------+------------+
| **1.1.1**  | * Fix unicode warning                                                  | 2018/09/26 |
+------------+------------------------------------------------------------------------+------------+
| **1.1.0**  | * Add degree symbol to segment mapper charmap                          | 2018/09/18 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.8**  | * Use DMA channel 10 (rather than ch. 5) for WS2812 NeoPixels          | 2018/01/23 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.7**  | * Use ``extras_require`` in ``setup.py`` for ARM dependencies          | 2017/11/26 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.6**  | * Version number available as ``luma.led_matrix.__version__`` now      | 2017/11/23 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.5**  | * Conditionally install WS2812 packages if Linux/ARM7L only            | 2017/10/22 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.4**  | * Make wheel universal                                                 | 2017/10/22 |
|            | * Minor documentation fixes                                            |            |
+------------+------------------------------------------------------------------------+------------+
| **1.0.3**  | * Explicitly state 'UTF-8' encoding in setup when reading files        | 2017/10/18 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.2**  | * Setup fails due to programmer not understanding basic Python ...     | 2017/08/05 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.1**  | * Setup on Python 3 fails due to hyphen in package name                | 2017/08/05 |
+------------+------------------------------------------------------------------------+------------+
| **1.0.0**  | * Stable release (remove all deprecated methods & parameters)          | 2017/07/30 |
+------------+------------------------------------------------------------------------+------------+
| **0.11.1** | * Add Python3 compatibility for neopixels/neosegments                  | 2017/07/29 |
+------------+------------------------------------------------------------------------+------------+
| **0.11.0** | * Alternative WS2812 low level implementation                          | 2017/07/21 |
|            | * Add support for @msurguy's modular NeoSegments                       |            |
+------------+------------------------------------------------------------------------+------------+
| **0.10.1** | * Add block_orientation=180 option                                     | 2017/05/01 |
+------------+------------------------------------------------------------------------+------------+
| **0.10.0** | * **BREAKING CHANGE:** Move sevensegment class to                      | 2017/04/22 |
|            |   ``luma.core.virtual`` package                                        |            |
+------------+------------------------------------------------------------------------+------------+
| **0.9.0**  | * Add support for APA102 RGB neopixels                                 | 2017/03/30 |
+------------+------------------------------------------------------------------------+------------+
| **0.8.0**  | * Change MAX7219's block_orientation to support ±90° angle correction  | 2017/03/19 |
|            | * Deprecate "vertical" and "horizontal" block_orientation              |            |
+------------+------------------------------------------------------------------------+------------+
| **0.7.0**  | * **BREAKING CHANGE:** Move sevensegment class to                      | 2017/03/04 |
|            |   ``luma.led_matrix.virtual`` package                                  |            |
|            | * Documentation updates & corrections                                  |            |
+------------+------------------------------------------------------------------------+------------+
| **0.6.2**  | * Allow MAX7219 and NeoPixel driver constructors to accept any args    | 2017/03/02 |
+------------+------------------------------------------------------------------------+------------+
| **0.6.1**  | * Restrict exported Python symbols from ``luma.led_matrix.device``     | 2017/03/02 |
+------------+------------------------------------------------------------------------+------------+
| **0.6.0**  | * Add support for arbitrary MxN matrices rather than a single chain    | 2017/02/22 |
+------------+------------------------------------------------------------------------+------------+
| **0.5.3**  | * Huge performance improvements for cascaded MAX7219 devices           | 2017/02/21 |
|            | * Documentation updates                                                |            |
+------------+------------------------------------------------------------------------+------------+
| **0.5.2**  | * Add apostrophe representation to seven-segment display               | 2017/02/19 |
|            | * Deprecate ``luma.led_matrix.legacy`` (moved to ``luma.core.legacy``) |            |
+------------+------------------------------------------------------------------------+------------+
| **0.4.4**  | * Support both common-row anode and common-row cathode LED matrices    | 2017/02/02 |
+------------+------------------------------------------------------------------------+------------+
| **0.4.3**  | * Add translation mapping to accomodate Pimoroni's 8x8 Unicorn HAT     | 2017/01/29 |
|            | * MAX7219 optimizations                                                |            |
+------------+------------------------------------------------------------------------+------------+
| **0.4.2**  | * Fix bug in neopixel initialization                                   | 2017/01/27 |
|            | * Improved demo scripts                                                |            |
|            | * Additional tests                                                     |            |
+------------+------------------------------------------------------------------------+------------+
| **0.4.0**  | * Add support for WS2812 NeoPixel strips/arrays                        | 2017/01/23 |
+------------+------------------------------------------------------------------------+------------+
| **0.3.3**  | * Fix for dot muncher: not handling full-stop at line end              | 2017/01/21 |
|            | * Documentation updates                                                |            |
+------------+------------------------------------------------------------------------+------------+
| **0.3.2**  | * Replace bytearray with ``mutable_string`` implementation             | 2017/01/20 |
|            | * More tests                                                           |            |
+------------+------------------------------------------------------------------------+------------+
| **0.3.1**  | * Python 3 compatibility (fix exception in bytearray creation)         | 2017/01/20 |
|            | * Begin to add tests & test infrastructure                             |            |
+------------+------------------------------------------------------------------------+------------+
| **0.3.0**  | * **BREAKING CHANGE:** Package rename to ``luma.led_matrix``           | 2017/01/19 |
+------------+------------------------------------------------------------------------+------------+
| **0.2.3**  | * Bit-bang version using wiringPi                                      | 2013/01/28 |
+------------+------------------------------------------------------------------------+------------+
