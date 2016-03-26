%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: Plasma simple systray
Name: simplesystray
Version: 5.6.0
Release: 1
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Emoticons)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Attica)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(LibKWorkspace)
BuildRequires: cmake(LibTaskManager)
BuildRequires: cmake(KWinDBusInterface)
BuildRequires: cmake(ScreenSaverDBusInterface)
BuildRequires: cmake(KRunnerAppDBusInterface)
BuildRequires: cmake(KSMServerDBusInterface)
BuildRequires: pkgconfig(packagekitqt5)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Concurrent)

%description
An experimental Plasma systray.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray.experimental
%{_libdir}/qt5/plugins/plasma/applets/org.kde.plasma.*.so
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.*.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray/*
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray.experimental/*
