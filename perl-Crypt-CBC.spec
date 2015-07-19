%define	modname	Crypt-CBC
%define modver 2.33

Summary:	Encrypt Data with Cipher Block Chaining Mode
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Crypt/Crypt-CBC-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Crypt::Blowfish_PP)
BuildRequires:	perl(Crypt::CAST5)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Crypt::IDEA)

%description
This module is a Perl-only implementation of the cryptographic cipher
block chaining mode (CBC).  In combination with a block cipher such as
DES or IDEA, you can encrypt and decrypt messages of arbitrarily long
length.  The encrypted messages are compatible with the encryption
format used by SSLeay, and can be made compatible with the newer
OpenSSL package by specifying the -salt argument.

To use this module, you will first create a Crypt::CBC cipher object with
new().  At the time of cipher creation, you specify an encryption key
to use and, optionally, a block encryption algorithm.  You will then
call the start() method to initialize the encryption or decryption
process, crypt() to encrypt or decrypt one or more blocks of data, and
lastly finish(), to pad and encrypt the final block.  For your
convenience, you can call the encrypt() and decrypt() methods to
operate on a whole data value at once.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README eg
%{perl_vendorlib}/Crypt
%{_mandir}/man3*/*


