
BuildArch:      noarch
Summary:        Java language server
Name:           jdtls
Version:        1.41.0
Release:        1%{?dist}

%global         timestamp  202410311350

License:        EPL-2.0
URL:            https://github.com/eclipse-jdtls/eclipse.jdt.ls
Source0:        https://www.eclipse.org/downloads/download.php?file=/jdtls/milestones/%{version}/jdt-language-server-%{version}-%{timestamp}.tar.gz

BuildRequires:  bash
Requires:       (java-headless >= 1:1.17.0 or java >= 1.17.0)

%description
The Eclipse JDT Language Server is a Java language specific implementation of the Language Server Protocol and can be used with any editor that supports the protocol, to offer good support for the Java Language.

%prep
%setup -c

%install
mkdir -p -m0755 %{buildroot}/opt
cp -r %{_builddir}/jdtls-%{version} %{buildroot}/opt/jdtls

mkdir -p -m0755 %{buildroot}%{_bindir}
ln -sr /opt/jdtls/bin/jdtls %{buildroot}%{_bindir}/jdtls

%files
/opt/jdtls
%{_bindir}/jdtls

%changelog
