Summary:	Small WebServer
Name:		monkey
Version:	0.21.0
Release:	1
License:	GPLv2
Group:		Networking/WWW
Source0:	http://www.monkey-project.com/releases/0.21/%{name}-%{version}.tar.gz
URL:		http://www.monkey-project.com

%description
Monkey HTTP Daemon is a very Fast and Lightweight Web Server for Linux.
It has been designed to be very scalable with low memory and CPU consumption,
 the perfect solution for embedded and high production environments. 


%prep
%setup -q

%build
sed -i -e '/$STRIP /d' -e 's/install -s -m 644/install -m 755/' configure
sed -i '/install -m 755 bin\/banana/d' configure || die "sed banana"


./configure	--default-port=80		\
		--prefix=%{_prefix}		\
		--sysconfdir=%{_sysconfdir}/monkey/	\
		--bindir=%{_prefix}/bin		\
		--mandir=%{_mandir}/man1/	\
		--plugdir=%{_libdir}/monkeyd/plugins	\
		--logdir=%{_logdir}
%make

%install
echo $(pwd)
%__install -m 755 -d %{buildroot}/%{_bindir}
%__install -m 755 -d %{buildroot}/%{_libdir}
%__install -m 755 -d %{buildroot}/%{_libdir}/monkeyd/plugins
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/auth
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/cheetah
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/dirlisting
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/dirlisting/themes/guineo
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/dirlisting/themes
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/logger
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/mandril
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/plugins/palm
%__install -m 755 -d %{buildroot}/%{_sysconfdir}/monkey/sites
%__install -m 755 -d %{buildroot}/%{_mandir}/man1

%__install -m 755 bin/monkey %{buildroot}/%{_bindir}
%__install -m 755 bin/banana %{buildroot}/%{_bindir}
%__install -m 644 man/*.1 %{buildroot}/%{_mandir}/man1

%__install -m 644 plugins/*/*.so %{buildroot}/%{_libdir}/monkeyd/
%__install -m 644 conf/monkey.*  %{buildroot}/%{_sysconfdir}/monkey/
%__install -m 644 conf/plugins.load  %{buildroot}/%{_sysconfdir}/monkey/
%__install -m 644 conf/sites/*  %{buildroot}/%{_sysconfdir}/monkey/sites
#% __install -m 644 conf/plugins/*  %{buildroot}/%{_sysconfdir}/monkey/plugins

%__install -m 644 conf/plugins/auth/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/auth/
%__install -m 644 conf/plugins/cheetah/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/cheetah/
%__install -m 644 conf/plugins/dirlisting/dirhtml.conf  %{buildroot}/%{_sysconfdir}/monkey/plugins/dirlisting/
%__install -m 644 conf/plugins/dirlisting/themes/guineo/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/dirlisting/themes/guineo/
%__install -m 644 conf/plugins/logger/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/logger/
%__install -m 644 conf/plugins/mandril/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/mandril/
%__install -m 644 conf/plugins/palm/*  %{buildroot}/%{_sysconfdir}/monkey/plugins/palm/


%files

%{_bindir}/%{name}
%{_bindir}/banana
%{_libdir}/monkeyd/%{name}-auth.so
%{_libdir}/monkeyd/%{name}-cheetah.so
%{_libdir}/monkeyd/%{name}-dirlisting.so
%{_libdir}/monkeyd/%{name}-liana.so
%{_libdir}/monkeyd/%{name}-logger.so
%{_libdir}/monkeyd/%{name}-mandril.so
%{_libdir}/monkeyd/%{name}-palm.so
%{_sysconfdir}/monkey/monkey.*
%{_sysconfdir}/monkey/plugins.load
%{_sysconfdir}/monkey/sites/*
%{_sysconfdir}/monkey/plugins/auth
%{_sysconfdir}/monkey/plugins/cheetah
%{_sysconfdir}/monkey/plugins/dirlisting
%{_sysconfdir}/monkey/plugins/logger
%{_sysconfdir}/monkey/plugins/mandril
%{_sysconfdir}/monkey/plugins/palm
%{_mandir}/man1/*
