%define upstream_name    DBIx-Class-DeploymentHandler
%define upstream_version 0.001005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Extensible DBIx::Class deployment
License:	GPL+ or Artistic
Group:		Development/Perl
Url:    	https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Carp::Clan)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Touch)
BuildRequires:	perl(Log::Contextual)
BuildRequires:	perl(Method::Signatures::Simple)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(aliased)
BuildRequires:	perl(autodie)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
'DBIx::Class::DeploymentHandler' is, as its name suggests, a tool for
deploying and upgrading databases with DBIx::Class. It is
designed to be much more flexible than DBIx::Class::Schema::Versioned,
hence the use of Moose and lots of roles.

'DBIx::Class::DeploymentHandler' itself is just a recommended set of roles
that we think will not only work well for everyone, but will also yield the
best overall mileage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.5-1mdv2011.0
+ Revision: 654059
- update to new version 0.001005

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.1.4-4
+ Revision: 653560
- rebuild for updated spec-helper

  + Shlomi Fish <shlomif@mandriva.org>
    - Fix the summary and description

* Fri Aug 13 2010 Shlomi Fish <shlomif@mandriva.org> 0.1.4-2mdv2011.0
+ Revision: 569490
- Add a missing build-requires (thanks to Anssi)
- import perl-DBIx-Class-DeploymentHandler


* Tue Jul 27 2010 cpan2dist 0.001003-1mdv
- initial mdv release, generated with cpan2dist
