#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jline
Version  : 2.14.6
Release  : 3
URL      : https://github.com/jline/jline2/archive/jline-2.14.6.tar.gz
Source0  : https://github.com/jline/jline2/archive/jline-2.14.6.tar.gz
Source1  : https://repo1.maven.org/maven2/jline/jline/0.9.94/jline-0.9.94.jar
Source2  : https://repo1.maven.org/maven2/jline/jline/0.9.94/jline-0.9.94.pom
Source3  : https://repo1.maven.org/maven2/jline/jline/1.0/jline-1.0.jar
Source4  : https://repo1.maven.org/maven2/jline/jline/1.0/jline-1.0.pom
Source5  : https://repo1.maven.org/maven2/jline/jline/2.14.6/jline-2.14.6.jar
Source6  : https://repo1.maven.org/maven2/jline/jline/2.14.6/jline-2.14.6.pom
Source7  : https://repo1.maven.org/maven2/org/jline/jline-parent/3.9.0/jline-parent-3.9.0.pom
Source8  : https://repo1.maven.org/maven2/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.jar
Source9  : https://repo1.maven.org/maven2/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.pom
Source10  : https://repo1.maven.org/maven2/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.jar
Source11  : https://repo1.maven.org/maven2/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mvn-jline-data = %{version}-%{release}
Requires: mvn-jline-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
<!--
This software is distributable under the BSD license. See the terms of the
BSD license in the documentation provided with this software.

%package data
Summary: data components for the mvn-jline package.
Group: Data

%description data
data components for the mvn-jline package.


%package license
Summary: license components for the mvn-jline package.
Group: Default

%description license
license components for the mvn-jline package.


%prep
%setup -q -n jline2-jline-2.14.6

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jline
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jline/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/0.9.94
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/jline/jline/0.9.94/jline-0.9.94.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/0.9.94
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/jline/jline/0.9.94/jline-0.9.94.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/1.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/jline/jline/1.0/jline-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/1.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/jline/jline/1.0/jline-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/2.14.6
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/jline/jline/2.14.6/jline-2.14.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/jline/jline/2.14.6
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/jline/jline/2.14.6/jline-2.14.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-parent/3.9.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-parent/3.9.0/jline-parent-3.9.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/jline/jline/0.9.94/jline-0.9.94.jar
/usr/share/java/.m2/repository/jline/jline/0.9.94/jline-0.9.94.pom
/usr/share/java/.m2/repository/jline/jline/1.0/jline-1.0.jar
/usr/share/java/.m2/repository/jline/jline/1.0/jline-1.0.pom
/usr/share/java/.m2/repository/jline/jline/2.14.6/jline-2.14.6.jar
/usr/share/java/.m2/repository/jline/jline/2.14.6/jline-2.14.6.pom
/usr/share/java/.m2/repository/org/jline/jline-parent/3.9.0/jline-parent-3.9.0.pom
/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.jar
/usr/share/java/.m2/repository/org/jline/jline-reader/3.9.0/jline-reader-3.9.0.pom
/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.jar
/usr/share/java/.m2/repository/org/jline/jline-terminal/3.9.0/jline-terminal-3.9.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jline/LICENSE.txt
