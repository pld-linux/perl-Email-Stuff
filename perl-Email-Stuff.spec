#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Stuff
Summary:	Email::Stuff - email stuff to people and things... and, like, stuff
Summary(pl):	Email::Stuff - rzeczy zwi�zane z e-mailami itp.
Name:		perl-Email-Stuff
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	73497a6d516c6024c1d93491ad5c132c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Clone >= 0.13
BuildRequires:	perl-Email-MIME >= 1.6
BuildRequires:	perl-Email-MIME-Creator >= 1.3
BuildRequires:	perl-Email-Send >= 1.42
BuildRequires:	perl-File-Slurp >= 9999.04
BuildRequires:	perl-File-Type >= 0.22
BuildRequires:	perl-prefork >= 0.02
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

%description -l pl
Email::Stuff, tak jak nazwa sugeruje, to do�� przypadkowy modu�
u�ywany do wysy�ania "rzeczy" do ludzi przy u�yciu najbardziej
popularnych metod. Jest to raczej wysokopoziomowy modu� zaprojektowany
w celu u�atwienia u�ycia, ale zaimplementowany w oparciu o zwi�z�e i
poprawne modu�y Email::.

Email::Stuff jest typowo u�ywany do tworzenia list�w i wysy�ania ich
w jednej instrukcji. I jest pewny tylko przy u�ywaniu do tworzenia i
wysy�ania list�w. Jako taki nie zawiera zerow� obs�ug� parsowania i
niewielk� obs�ug� modyfikacji. Jeszcze raz - jest to modu� to sytuacji
typu "sklej to razem i wy�lij", ale b�d�cy jeszcze w stanie zrobi� to
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
