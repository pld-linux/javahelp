# TODO
# - compile from src.jar
#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
Summary:	JavaHelp - online help system
Summary(pl.UTF-8):	JavaHelp - system pomocy online
Name:		javahelp
Version:	2.0.05
Release:	0.3
Epoch:		0
License:	restricted, non-distributable (Sun Binary Code License)
Group:		Development/Languages/Java
Source0:	%{name}-2_0_05.zip
# NoSource0-md5:	b9b12989471f5858c982154335e1cc96
NoSource:	0
URL:		http://java.sun.com/products/javahelp/index.jsp
BuildRequires:	jpackage-utils >= 0:1.5
BuildRequires:	rpm-javaprov
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

%description -l pl.UTF-8
JavaHelp to program z dostępnym kodem źródłowym będący w pełni
funkcjonalnym, niezależnym od platformy, rozszerzalnym systemem
pomocy pozwalającym umieszczać pomoc online w apletach, komponentach,
aplikacjach, systemach operacyjnych i urządzeniach. Autorzy mogą także
używać systemu JavaHelp do udostępniania dokumentacji online przez WWW
i w sieciach korporacyjnych.

%package manual
Summary:	Manual for JavaHelp
Summary(pl.UTF-8):	Podręcznik do systemu JavaHelp
Group:		Development/Languages/Java

%description manual
Manual for JavaHelp.

%description manual -l pl.UTF-8
Podręcznik do systemu JavaHelp.

%package javadoc
Summary:	Javadoc for JavaHelp
Summary(pl.UTF-8):	Dokumentacja Javadoc do systemu JavaHelp
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for JavaHelp.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do systemu JavaHelp.

%package demo
Summary:	Demo for JavaHelp
Summary(pl.UTF-8):	Przykłady użycia systemu JavaHelp
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for JavaHelp.

%description demo -l pl.UTF-8
Przykłady użycia systemu JavaHelp.

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

install javahelp/lib/jhall.jar $RPM_BUILD_ROOT%{_javadir}/jhall-%{version}.jar
install javahelp/lib/jh.jar $RPM_BUILD_ROOT%{_javadir}/jh-%{version}.jar
install javahelp/lib/jhbasic.jar $RPM_BUILD_ROOT%{_javadir}/jhbasic-%{version}.jar
install javahelp/lib/jsearch.jar $RPM_BUILD_ROOT%{_javadir}/jsearch-%{version}.jar
ln -s jhall-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jhall.jar
ln -s jh-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jh.jar
ln -s jhbasic-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jhbasic.jar
ln -s jsearch-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jsearch.jar
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
%{_javadir}/*.jar
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
