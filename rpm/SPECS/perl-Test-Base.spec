Name:           perl-Test-Base
Version:        0.88
Release:        5%{?dist}
Summary:        Data Driven Testing Framework
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Base/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Test-Base-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:v5.8.1
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(Spiffy)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Test::More)
Requires:       perl(Filter::Util::Call)
Requires:       perl(Spiffy)
Requires:       perl(Test::Deep)
Requires:       perl(Test::More)
Provides:       perl(Test::Base)

%description
Testing is usually the ugly part of Perl module authoring. Perl gives you a
standard way to run tests with Test::Harness, and basic testing primitives
with Test::More. After that you are pretty much on your own to develop a
testing framework and philosophy. Test::More encourages you to make your
own framework by subclassing Test::Builder, but that is not trivial.

%prep
%setup -q -n Test-Base-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun May 21 2017 Yichun Zhang (agentzh) <yichun@openresty.com> 0.88-2
- added misssing build dep and runtime dep, Test::More.
* Sun May 21 2017 Yichun Zhang (agentzh) <yichun@openresty.com> 0.88-1
- Specfile autogenerated by cpanspec 1.78.
