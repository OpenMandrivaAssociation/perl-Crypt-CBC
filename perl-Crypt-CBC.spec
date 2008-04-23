%define	module	Crypt-CBC
%define name	perl-%{module}
%define version	2.29
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Encrypt Data with Cipher Block Chaining Mode
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%module/
Source:		http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Crypt::Blowfish_PP)
BuildRequires:	perl(Crypt::CAST5)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Crypt::IDEA)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make


%check
%{__make} test

%install
rm -rf %{buildroot} 
%{makeinstall_std}

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README eg
%{perl_vendorlib}/Crypt
%{_mandir}/man3*/*

