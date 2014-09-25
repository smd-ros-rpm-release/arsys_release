Name:           ros-hydro-ar-sys
Version:        1.0.3
Release:        1%{?dist}
Summary:        ROS ar_sys package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ar_sys
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs

%description
3D pose estimation ROS package using ArUco marker boards.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Sep 26 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.3-1
- Autogenerated by Bloom

* Tue Sep 23 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.2-3
- Autogenerated by Bloom

* Tue Sep 23 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.2-1
- Autogenerated by Bloom

* Tue Sep 23 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.2-0
- Autogenerated by Bloom

* Tue Sep 23 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.3-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Hamdi Sahloul <sahloul@race.u-tokyo.ac.jp> - 1.0.2-2
- Autogenerated by Bloom

