Summary:	Norman Walsh's modular stylesheets for DocBook
Summary(pl):	Arkusze stylistyczne XSL dla DocBook DTD
Summary(pt_BR):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.61.3
Release:	1
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://dl.sourceforge.net/sourceforge/docbook/docbook-xsl-%{version}.tar.gz
# Source0-md5:	dc91b494e0afc586482c17e9373c0c56
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
BuildRequires:	/usr/bin/xmlcatalog
Requires(post,postun): /usr/bin/xmlcatalog
Requires(post,postun): /etc/xml/catalog
Requires:	/etc/xml/catalog
Requires:	sgml-common >= 0.5
AutoReqProv:	0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# think about _javaclassdir location
#%define		_javaclassdir	%{_datadir}/java/classes
%define xsl_path %{_datadir}/sgml/docbook/xsl-stylesheets
%define catalog  %{xsl_path}/catalog.xml

%description
Highly customizable XSL stylesheets for DocBook XML DTD. The
stylesheets allow to produce documents in XSL FO, HTML or XHTML
formats.

%description -l pl
Konfigurowalne arkusze stylistyczne dla DocBook XML DTD. Arkusze
stylistyczne, zawarte w tym pakiecie, umo¿liwiaj± tworzenie dokumentów
w formacie XSL FO, HTML lub XHTML.

%description -l pt_BR
Stylesheets modulares do Norman Walsh para DocBook.

%prep
%setup -q -n docbook-xsl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{xsl_path},%{_sysconfdir}/xml} \
#	$RPM_BUILD_ROOT%{_javaclassdir}
install -d $RPM_BUILD_ROOT{%{xsl_path},%{_sysconfdir}/xml}

cp -a * $RPM_BUILD_ROOT%{xsl_path}

#install extensions/*.jar $RPM_BUILD_ROOT%{_javaclassdir}

%xmlcat_create $RPM_BUILD_ROOT%{catalog}
 
%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/%{version} file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}
%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/current file://%{xsl_path} $RPM_BUILD_ROOT%{catalog}

rm -rf $RPM_BUILD_ROOT%{xsl_path}/doc \
	$RPM_BUILD_ROOT%{xsl_path}/BUGS \
	$RPM_BUILD_ROOT%{xsl_path}/ChangeLog \
	$RPM_BUILD_ROOT%{xsl_path}/README \
	$RPM_BUILD_ROOT%{xsl_path}/RELEASE-NOTES.html \
	$RPM_BUILD_ROOT%{xsl_path}/RELEASE-NOTES.xml \
	$RPM_BUILD_ROOT%{xsl_path}/TODO \
	$RPM_BUILD_ROOT%{xsl_path}/WhatsNew \
	$RPM_BUILD_ROOT%{xsl_path}/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%pre 
if [ -L %{xsl_path} ] ; then
	rm -rf %{xsl_path}
fi

%post
if ! grep -q %{catalog} /etc/xml/catalog ; then
    %xmlcat_add %{catalog}

fi 
 
%preun
if [ "$1" = "0" ] ; then
    %xmlcat_del %{catalog}

fi

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README RELEASE-NOTES.*
#%%{_javaclassdir}/*
%{xsl_path}
