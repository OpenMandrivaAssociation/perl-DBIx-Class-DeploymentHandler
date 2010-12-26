%define upstream_name    DBIx-Class-DeploymentHandler
%define upstream_version 0.001004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Extensible DBIx::Class deployment
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Touch)
BuildRequires: perl(Log::Contextual)
BuildRequires: perl(Method::Signatures::Simple)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(SQL::Translator)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(aliased)
BuildRequires: perl(autodie)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


