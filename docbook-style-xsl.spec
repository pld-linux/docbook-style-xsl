Summary:	Modular DocBook Stylesheets
Summary(es):	Norman Walsh's modular stylesheets for DocBook
Summary(pl):	Arkusze stylistyczne XSL dla DocBook DTD
Summary(pt_BR):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.54.1
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-xsl-%{version}.tar.gz
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
Requires:	sgml-common >= 0.5
BuildArch:	noarch
AutoReqProv:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java/classes

%description
XSL is a stylesheet language for both print and online rendering.
There is XSL stylesheets for DocBook DTD.

%description -l es
These XSL stylesheets allow to produce XSL FO trees or HTML / XHTML
with any DocBook XML document. They are highly customizable.

%description -l pl
docbook-xsl jest zbiorem arkuszy stylistycznych pozwalaj±cych
przekszta³ciæ dokument napisany w DocBook DTD na prezentacjê on-line
(wykorzystuj±c HTML) lub na drukowany dokument.

%description -l pt_BR
Stylesheets modulares do Norman Walsh para DocBook.

%prep
%setup -q -n docbook-xsl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets \
	$RPM_BUILD_ROOT%{_javaclassdir}

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets

install extensions/*.jar $RPM_BUILD_ROOT%{_javaclassdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/doc \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/BUGS \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/ChangeLog \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/README \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/RELEASE-NOTES.html \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/RELEASE-NOTES.xml \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/TODO \
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets/WhatsNew \


%clean
rm -rf $RPM_BUILD_ROOT

%pre 
if [ -L %{_datadir}/sgml/docbook/xsl-stylesheets ] ; then
	rm -rf %{_datadir}/sgml/docbook/xsl-stylesheets
fi


%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README RELEASE-NOTES.*
%{_javaclassdir}/*
%dir %{_datadir}/sgml/docbook/xsl-stylesheets
%{_datadir}/sgml/docbook/xsl-stylesheets/VERSION
%{_datadir}/sgml/docbook/xsl-stylesheets/common
%{_datadir}/sgml/docbook/xsl-stylesheets/docsrc
%{_datadir}/sgml/docbook/xsl-stylesheets/extensions
%{_datadir}/sgml/docbook/xsl-stylesheets/fo
%{_datadir}/sgml/docbook/xsl-stylesheets/html
%{_datadir}/sgml/docbook/xsl-stylesheets/htmlhelp
%{_datadir}/sgml/docbook/xsl-stylesheets/images
%{_datadir}/sgml/docbook/xsl-stylesheets/javahelp
%{_datadir}/sgml/docbook/xsl-stylesheets/lib
%{_datadir}/sgml/docbook/xsl-stylesheets/params
%{_datadir}/sgml/docbook/xsl-stylesheets/profiling
%{_datadir}/sgml/docbook/xsl-stylesheets/template
%{_datadir}/sgml/docbook/xsl-stylesheets/tools
%{_datadir}/sgml/docbook/xsl-stylesheets/xhtml
%{_datadir}/sgml/docbook/xsl-stylesheets/manpages
