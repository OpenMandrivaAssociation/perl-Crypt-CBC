%define	upstream_name	 Crypt-CBC
%define upstream_version 2.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Encrypt Data with Cipher Block Chaining Mode
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Crypt::Blowfish_PP)
BuildRequires:	perl(Crypt::CAST5)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(Crypt::IDEA)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.300.0-5mdv2012.0
+ Revision: 765122
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.300.0-4
+ Revision: 763619
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.300.0-3
+ Revision: 676566
- rebuild
- rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.300.0-1mdv2011.0
+ Revision: 403030
- rebuild using %%perl_convert_version

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.30-1mdv2009.1
+ Revision: 292038
- update to new version 2.30

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.29-2mdv2009.0
+ Revision: 268403
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.29-1mdv2009.0
+ Revision: 196822
- update to new version 2.29

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.28-1mdv2009.0
+ Revision: 194923
- update to new version 2.28

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.24-1mdv2008.1
+ Revision: 97433
- update to new version 2.24

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 2.22-1mdv2008.0
+ Revision: 19825
- 2.22


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.19-1mdv2007.0
- New version 2.19

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2007.0
- New release 2.18
- better source URL

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.17-1mdk
- New release 2.17
- spec cleanup

* Wed Aug 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.15-1mdk
- New release 2.15

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.14-2mdk
- fix deps, summary and description

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.14-1mdk
- 2.14
- Make rpmbuildable

* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.12-1mdk
- 2.12

* Fri Jun 04 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.11-1mdk
- rebuild for new perl
- don't use PREFIX
- use %%makeinstall_std macro
- cosmetics

