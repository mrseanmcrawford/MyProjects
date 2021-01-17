//
//  assignmentApp.swift
//  Shared
//
//  Created by Sean Crawford on 1/8/21.
//

import SwiftUI

@main
struct assignmentApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: assignmentDocument()) { file in
            ContentView(document: file.$document)
        }
    }
}
