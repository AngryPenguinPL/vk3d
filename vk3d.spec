%define	major 1
%define	libname %mklibname vkd3d %{major}
%define	devname %mklibname vkd3d -d
%define	libname_utils %mklibname vkd3d-utils %{major}
%define	devname_utils %mklibname vkd3d-utils -d

Summary:	Vulkan layer for Direct3D 12
Name:		vkd3d
Version:	1.0
Release:	1
License:	GPLv2
Group:		Emulators
Url:		https://dl.winehq.org/vkd3d
Source0:	https://dl.winehq.org/vkd3d/source/%{name}-%{version}.tar.xz
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(xcb-keysyms)

Requires:	%{libname} = %{EVRD}
Requires:	%{libname_utils} = %{EVRD}

%description
Vulkan layer for support Direct3D 12 in wine

%files
%doc AUTHORS COPYING LICENSE README

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The vkd3d 3D Graphics Library
Group:		System/Libraries

%description -n %{libname}
This package contains the vkd3d 3D Graphics Library.

%files -n %{libname}
%doc LICENSE
%{_libdir}/libvkd3d.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libname_utils}
Summary:	The vkd3d 3D Graphics Utility Library
Group:		System/Libraries

%description -n %{libname_utils}
This package contains the vkd3d 3D Graphics Utility Library.

%files -n %{libname_utils}
%doc LICENSE
%{_libdir}/libvkd3d-utils.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C
Requires:	%{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development files for Vulkan applications.

%files -n %{devname}
%doc LICENSE
%{_includedir}/%{name}/%{name}.h
%{_includedir}/%{name}/%{name}_d*.h
%{_includedir}/%{name}/%{name}_w*.h
%{_libdir}/libvkd3d.a
%{_libdir}/libvkd3d.so
%{_libdir}/pkgconfig/libvkd3d.pc

#----------------------------------------------------------------------------

%package -n %{devname_utils}
Summary:	Development files for %{libname_utils}
Group:		Development/C
Requires:	%{name} = %{EVRD}
Requires:	%{libname_utils} = %{EVRD}
Provides:	%{name}-utils-devel = %{EVRD}

%description -n %{devname_utils}
This package contains the development files for Vulkan applications.

%files -n %{devname_utils}
%doc LICENSE
%{_includedir}/%{name}/%{name}_utils.h
%{_libdir}/libvkd3d-utils.a
%{_libdir}/libvkd3d-utils.so
%{_libdir}/pkgconfig/libvkd3d-utils.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

