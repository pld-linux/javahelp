# TODO
# - compile from src.jar
# - some specific License name? not Open Source as have to accept EULA when downloading?
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
Summary:	JavaHelp
Name:		javahelp
Version:	2.0.05
Release:	0.1
Epoch:		0
License:	Open Source
Group:		Development/Languages/Java
URL:		http://java.sun.com/products/javahelp/index.jsp
Source0:	%{name}-2_0_05.zip
# Source0-md5:	b9b12989471f5858c982154335e1cc96
NoSource:	0
BuildRequires:	jpackage-utils >= 0:1.5
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils >= 0:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaHelp is an open source software, a full-featured,
platform-independent, extensible help system that enables you to
incorporate online help in applets, components, applications,
operating systems, and devices. Authors can also use the JavaHelp
software to deliver online documentation for the Web and corporate
intranet.

%package manual
Summary:	Manual for %{name}
Group:		Development/Languages/Java

%description manual
Documentation for %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%package demo
Summary:	Demo for %{name}
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n jh2.0
find -name '.svn' | xargs rm -rf

# prevent javadoc being included in doc
mv doc/api apidocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_bindir},%{_datadir}/%{name}}
install javahelp/bin/jhindexer $RPM_BUILD_ROOT%{_bindir}/jhindexer
install javahelp/bin/jhsearch $RPM_BUILD_ROOT%{_bindir}/jhsearch

install javahelp/lib/jhall.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -a javahelp/lib/dtd $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a demos $RPM_BUILD_ROOT%{_datadir}/%{name}

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc README README.html
%attr(755,root,root) %{_bindir}/*
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd

%files manual
%defattr(644,root,root,755)
%doc doc/*

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
%endif

%files demo
%defattr(644,root,root,755)
%{_datadir}/%{name}/demos
