Summary:	Modular DocBook Stylesheets
Summary(es):	Norman Walsh's modular stylesheets for DocBook
Summary(pl):	Arkusze stylistyczne XSL dla DocBook DTD
Summary(pt_BR):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.50.0
Release:	3
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-xsl-%{version}.tar.gz
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
Requires(post):	/usr/bin/xmlcatalog
Requires(preun):/usr/bin/xmlcatalog
BuildArch:	noarch
AutoReqProv:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define xsl_path %{_datadir}/sgml/docbook/xsl-stylesheets-%{version}

# please look into docbook-dtd42-xml.spec
%define xmlcat_add_rewrite()	/usr/bin/xmlcatalog --noout --add rewriteSystem %1 %2 %3
%define xmlcat_del()			/usr/bin/xmlcatalog --noout --del %1 /etc/xml/catalog

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
install -d $RPM_BUILD_ROOT%{xsl_path}

cp -a * $RPM_BUILD_ROOT%{xsl_path}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
 
	%xmlcat_add_rewrite http://docbook.sourceforge.net/release/xsl/%{version} file://%{xsl_path} /etc/xml/catalog

fi

%preun
if [ "$1" = "0" ]; then

	%xmlcat_del http://docbook.sourceforge.net/release/xsl/%{version}

fi

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README
%dir %{xsl_path}
#%attr(755,root,root) %{xsl_path}/bin/*.pl
%{xsl_path}/VERSION
%{xsl_path}/common
#%{xsl_path}/contrib
#%{xsl_path}/doc
#%{xsl_path}/docsrc
%{xsl_path}/extensions
%{xsl_path}/fo
%{xsl_path}/html
%{xsl_path}/images
#%{xsl_path}/indexing
%{xsl_path}/javahelp
%{xsl_path}/lib
%{xsl_path}/template
%{xsl_path}/xhtml
