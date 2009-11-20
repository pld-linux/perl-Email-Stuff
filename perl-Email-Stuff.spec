#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Stuff
Summary:	Email::Stuff - email stuff to people and things... and, like, stuff
Summary(pl.UTF-8):	Email::Stuff - rzeczy związane z e-mailami itp.
Name:		perl-Email-Stuff
Version:	2.101
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e789fe76edfeab07febc359341a59960
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME >= 1.901
BuildRequires:	perl-Email-Send >= 2.185
BuildRequires:	perl-Email-Simple >= 1.998
BuildRequires:	perl-File-Type >= 0.22
BuildRequires:	perl-Params-Util >= 0.23
BuildRequires:	perl-prefork >= 1.01
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Stuff, as its name suggests, is a fairly casual module used to
email "stuff" to people using the most common methods. It is a fairly
high-level module designed for ease of use, but implemented on top of
the tight and correct Email:: modules.

Email::Stuff is typically used to build emails and send them in a
single statement. And it is certain only for use when creating and
sending emails. As such, it contains no parsing support, and little
modification support. To re-iterate, this is very much a module for
those "slap it together and send it off" situations, but that still
has enough grunt behind the scenes to do things properly.

%description -l pl.UTF-8
Email::Stuff, tak jak nazwa sugeruje, to dość przypadkowy moduł
używany do wysyłania "rzeczy" do ludzi przy użyciu najbardziej
popularnych metod. Jest to raczej wysokopoziomowy moduł zaprojektowany
w celu ułatwienia użycia, ale zaimplementowany w oparciu o zwięzłe i
poprawne moduły Email::.

Email::Stuff jest typowo używany do tworzenia listów i wysyłania ich
w jednej instrukcji. I jest pewny tylko przy używaniu do tworzenia i
wysyłania listów. Jako taki nie zawiera zerową obsługę parsowania i
niewielką obsługę modyfikacji. Jeszcze raz - jest to moduł to sytuacji
typu "sklej to razem i wyślij", ale będący jeszcze w stanie zrobić to
poprawnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}::%{pnam}")' \
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
%doc Changes
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
