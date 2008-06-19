/** 
* @file Trigger_load.cxx
* @brief This is needed for forcing the linker to load all components
* of the library.
*
*  $Header: /nfs/slac/g/glast/ground/cvs/ConfigSvc/src/ConfigSvc_load.cxx,v 1.1.1.1 2008/06/12 02:02:32 echarles Exp $
*/

#include "GaudiKernel/DeclareFactoryEntries.h"

DECLARE_FACTORY_ENTRIES(ConfigSvc) {
    DECLARE_SERVICE( ConfigSvc );
} 

