As it's been a while since I programmed in Python, it took a bit of time to refresh myself with the syntax and differences of the language, however I believe I'm come to a satisfactory solution to the problem and it took me approximately 2 hours as per the requirement.

# Best Practices

Used VSCode and the Microsoft Python extension while writing this. As well output from pylint is below...

pylint app/main.py --disable C0330

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

pylint tests/main_test.py --disable C0330

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

# Usage
The program can be run as follows:

python3 app/main.py <arch>

```
python3 app/main.py amd64
1. devel/piglit: 51784
2. science/esys-particle: 18015
3. libdevel/libboost1.74-dev: 14332
4. math/acl2-books: 12668
5. golang/golang-1.15-src: 9015
6. libdevel/liboce-modeling-dev: 7457
7. net/zoneminder: 7002
8. libdevel/paraview-dev: 6178
9. kernel/linux-headers-5.10.0-20-amd64: 6162
10. kernel/linux-headers-5.10.0-18-amd64: 6156

```

# Test
There are two unit tests. One to test the download functionality by comparing the returned hash output of the downloaded file to the known hash. And a second the test that the actual parsing and statitics are correct by comparing program output to pre-computed output.

Run the tests-setup.sh script first to download the Content files to the tests directory (they were too large to include in git)

Testing can be run as follows:

python3 -m unittest tests/main_test.py

```
python3 -m unittest tests/main_test.py
.Testing arch i386 ---->
Skipping download in test environment.
1. devel/piglit: 51784
2. science/esys-particle: 18015
3. libdevel/libboost1.74-dev: 14332
4. math/acl2-books: 12660
5. golang/golang-1.15-src: 9015
6. libdevel/liboce-modeling-dev: 7457
7. net/zoneminder: 7002
8. kernel/linux-headers-5.10.0-18-rt-686-pae: 6187
9. kernel/linux-headers-5.10.0-20-rt-686-pae: 6187
10. kernel/linux-headers-5.10.0-18-686-pae: 6183
Testing arch arm64 ---->
Skipping download in test environment.
1. devel/piglit: 51784
2. science/esys-particle: 18015
3. libdevel/libboost1.74-dev: 14332
4. math/acl2-books: 12668
5. golang/golang-1.15-src: 9015
6. libdevel/liboce-modeling-dev: 7457
7. net/zoneminder: 7002
8. libdevel/paraview-dev: 6178
9. localization/locales-all: 5956
10. kernel/linux-headers-5.10.0-20-arm64: 5860
Testing arch amd64 ---->
Skipping download in test environment.
1. devel/piglit: 51784
2. science/esys-particle: 18015
3. libdevel/libboost1.74-dev: 14332
4. math/acl2-books: 12668
5. golang/golang-1.15-src: 9015
6. libdevel/liboce-modeling-dev: 7457
7. net/zoneminder: 7002
8. libdevel/paraview-dev: 6178
9. kernel/linux-headers-5.10.0-20-amd64: 6162
10. kernel/linux-headers-5.10.0-18-amd64: 6156
.
----------------------------------------------------------------------
Ran 2 tests in 7.077s

OK
```