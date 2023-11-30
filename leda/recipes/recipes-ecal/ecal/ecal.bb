SUMMARY = "Recipes for Eclipse-eCAL"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE.txt;md5=dbef9c501cb27a10080e3aaddcf0fb69"

SRC_URI += " \
gitsm://github.com/eclipse-ecal/ecal.git;protocol=https;nobranch=1 \
file://remove_qt5.patch \
file://rm_qt_sam.patch \
"

SRCREV = "edb152b96df902a732cac45cc9de5d8dcf7bbb0a"

S = "${WORKDIR}/git"

inherit cmake

DEPENDS += " \
git \
hdf5-native \
protobuf-native \
yaml-cpp-native \
"

RDEPENDS:${PN} = " \
hdf5 \
protobuf \
yaml-cpp \
"

do_configure() {
    cmake ${S} -DCMAKE_BUILD_TYPE=Release -DECAL_THIRDPARTY_BUILD_PROTOBUF=OFF -DECAL_THIRDPARTY_BUILD_CURL=OFF -DECAL_THIRDPARTY_BUILD_HDF5=OFF -DECAL_THIRDPARTY_BUILD_QWT=OFF
}

do_install:append() {
    install -d ${D}/usr/share
    mv ${D}/usr/local/share/* ${D}/usr/share

    install -d ${D}/etc
    mv ${D}/usr/local/etc/* ${D}/etc

    install -d ${D}/usr/lib
    mv ${D}/usr/local/lib/* ${D}/usr/lib

    install -d ${D}/usr/bin
    mv ${D}/usr/local/bin/* ${D}/usr/bin

    install -d ${D}/usr/include
    mv ${D}/usr/local/include/* ${D}/usr/include
    
    rm -rf ${D}/usr/local
}

FILES:${PN} = " \
/etc/ecal/ecaltime.ini \
/etc/ecal/ecal.ini \
/usr/share/ecal/samples/* \
/usr/lib/libecal* \
/usr/bin/ecal* \
"
