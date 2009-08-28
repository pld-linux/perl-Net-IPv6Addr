#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IPv6Addr
Summary:	Net::IPv6Addr - check validity of IPv6 addresses
Summary(pl.UTF-8):	Net::IPv6Addr - sprawdza poprawność adresów IPv6
Name:		perl-Net-IPv6Addr
Version:	0.2
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd06f0422ddb3ac119e2ef1e27aa9339
URL:		http://search.cpan.org/dist/Net-IPv6Addr/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Math::Base85)
BuildRequires:	perl(Net::IPv4Addr)
%endif
Suggests:	perl-Math-Base85
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IPv6Addr checks strings for valid IPv6 addresses, as specified in
RFC1884. You throw possible addresses at it, it either accepts them or
throws an exception.

If Math::Base85 is installed, then this module is able to process
addresses formatted in the style referenced by RFC1924.

%description -l pl.UTF-8
Net::IPv6Addr sprawdza ciągi znaków czy są
poprawnym adresem IPv6 tak jak zdefiniowano to w RFC1884.

We współpracy z modułem Math::Base85 moduł ten umożliwia przetworzenie
adresów zgodnych z formatem zdefiniowanym w RFC1924.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Net/*.pm
%{_mandir}/man3/*
