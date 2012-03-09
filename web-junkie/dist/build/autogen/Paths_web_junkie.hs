module Paths_web_junkie (
    version,
    getBinDir, getLibDir, getDataDir, getLibexecDir,
    getDataFileName
  ) where

import Data.Version (Version(..))
import System.Environment (getEnv)

version :: Version
version = Version {versionBranch = [0,1], versionTags = []}

bindir, libdir, datadir, libexecdir :: FilePath

bindir     = "/home/filipovskii_off/.cabal/bin"
libdir     = "/home/filipovskii_off/.cabal/lib/web-junkie-0.1/ghc-7.0.3"
datadir    = "/home/filipovskii_off/.cabal/share/web-junkie-0.1"
libexecdir = "/home/filipovskii_off/.cabal/libexec"

getBinDir, getLibDir, getDataDir, getLibexecDir :: IO FilePath
getBinDir = catch (getEnv "web_junkie_bindir") (\_ -> return bindir)
getLibDir = catch (getEnv "web_junkie_libdir") (\_ -> return libdir)
getDataDir = catch (getEnv "web_junkie_datadir") (\_ -> return datadir)
getLibexecDir = catch (getEnv "web_junkie_libexecdir") (\_ -> return libexecdir)

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir ++ "/" ++ name)
